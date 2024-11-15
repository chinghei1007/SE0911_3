import os.path
from tkinter import Tk, filedialog
import functions
import instructions as inst
class Gameboard:
    def __init__(self):
        self.defaultpath = functions.getDefaultPath()
        self.sqaures = inst.read_to_list(self.defaultpath) #[{name}{price}{rent}]


    def setup_board(self):
        for key in range(len(self.sqaures)):
            self.sqaures[key]["owned"] = -1 #no one owned any sqaures, if owned, change to corresponding
            #sqaures : [name] [price] [rent] [owned]
        #unit test 1109
        """for index, item in enumerate(self.sqaures):
            print(f"Item {index+1}: ")
            print(f"{item['name']}: ")
            print(f"{item['price']}: ")
            print(f"{item['rent']}: ")
            print(f"{item['owned']}: ")"""
        return self.sqaures

    def IsOwned(self,propertyName):
        for i, item in enumerate(self.sqaures):
            if propertyName in item['name'] and item['owned'] >= 0: return True
            if propertyName in item['name'] and item['owned'] < 0: return False
        print("IsOwned: property Not Found")

    def outputOwnedBy(self, position, playerNames): #playerNames, Game
        position -= 1
        propName = self.sqaures[position]['name'] #gameboard
        ownerID = self.sqaures[position]['owned']
        ownerName = ''
        if ownerID > 0:
            ownerName = playerNames[ownerID]
        else:
            ownerName = 'None'
        print(f"Owned by {ownerName}")

    def getProptertyList(self):
        return self.sqaures

    def printPropertyName(self,path): #test function
        with open(path, 'r') as file:
            lines = file.readlines()

            for i, line in enumerate(lines):
                name, price, rent = line.strip().split(',')
                rent = int(rent)

                if rent > 0:
                    print(f"{i+1}. {name}")

    def importGbfromFunc(self,path):
        self.sqaures = inst.read_to_list(path)

    """def exportGameboard(self, listDict):
        while True:
            file_path = input("Please enter the file path: ")
            if self.fileExist(file_path):
                print(f"File {file_path} already exists.")
                new_path = input("Please enter a new file name or path.")
                if self.fileExist(new_path):
                    print(f"{new_path} already exists, Please try again.")
                    continue
                if not inst.double_confirm():
                    print("Operation cancelled.")
                    return
                file_path = new_path
                file_path = os.path.abspath(file_path)
            break
        text = self.listDictToCommaDivided(listDict)
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text successfully exported to {file_path}") """

    def exportGameboard(self, listDict):
        root = Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(title="Select Location", defaultextension= ".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        root.destroy()

        if not file_path:
            print("No file selected. Operation cancelled.")
            return

        writeText = self.listDictToCommaDivided(listDict)
        with open(file_path, 'w') as f:
            f.write(writeText)

        print(f"Successfully written to {file_path}")

        file_path = os.path.abspath(file_path)

    def listDictToCommaDivided(self, listDict):
        lines = []
        for item in listDict:
            line = f"{item['name']},{item['price']},{item['rent']}"
            lines.append(line)
        return "\n".join(lines)

    def fileExist(self,path):
        return os.path.exists(path)

    def checkLineCount(self,text,linecount):
        lines = text.strip().split("\n")
        return len(lines) == linecount

    def checkFormat(self,text):
        lines = text.strip().split('\n')
        for line in lines:
            parts = line.split(',')
            if len(parts) != 3:
                print(f"Problem with {line} missing parts, it should be in format of str, int, int")
                return False
            elif not (parts[0].isalpha() and parts[1].isdigit() and parts[2].isdigit()):
                print(f"Problem with {line} format, it should be \"str, int, int\"")
                return False

        return True

    def check_Go_and_Jail(self,text):
        lines = text.strip().split('\n')
        go_count = sum(1 for line in lines if line.startswith('Go'))
        jail_count = sum(1 for line in lines if line.startswith('GoToJail'))
        if go_count > 1 or jail_count > 1:
            print("Please check only ONE go and ONE jail exists")
            return False
        return True