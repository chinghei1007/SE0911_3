import os.path
from tkinter import Tk, filedialog
import functions
import instructions as inst
from instructions import *
class Gameboard:
    def __init__(self):
        self.defaultpath = functions.getDefaultPath()
        self.sqaures = inst.read_to_list(self.defaultpath) #[{name}{price}{rent}]
        #self.sqaures = inst.read_to_list("property.txt")
        if not self.validate_board(self.sqaures):
            print("Board error, the game will now terminate, please contact gameboard designer or use the default board")
            raise SystemExit

    def reinitializeBoard(self,path):
        original = self.sqaures
        self.sqaures = inst.read_to_list(path) #[{name}{price}{rent}]
        #self.sqaures = inst.read_to_list("property.txt")
        if self.validate_board_noTerminate(self.sqaures):
            self.setup.board()
        else:
            print("Board invalid, Original Board would be used instead")
            self.sqaures = original



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

    def activateOwned(self, position, ID):
        self.sqaures[position-1]["owned"] = ID

    def IsOwned(self,position):
        propertyName = self.getPropertyName(position)
        for i, item in enumerate(self.sqaures):
            if propertyName in item['name'] and item['owned'] >= 0: return True
            if propertyName in item['name'] and item['owned'] < 0: return False
        print("IsOwned: property Not Found")

    def OwnedbyID(self,position):
        position -= 1
        prop_name = self.sqaures[position]['name']
        owner_id = self.sqaures[position]['owned']
        return owner_id

    def outputOwnedBy(self, position, player_names):
        position -= 1
        prop_name = self.sqaures[position]['name']
        owner_id = self.sqaures[position]['owned']
        if owner_id >= 0:
            return player_names[owner_id]
        else:
            return "None"

    def getProptertyList(self):
        return self.sqaures

    def printPropertyNamewithOwned(self, player_names):
        path = self.getDefaultPath()
        with open(path, 'r') as file:
            lines = file.readlines()

            for i, line in enumerate(lines):
                name, price, rent = line.strip().split(',')
                rent = int(rent)

                if rent > 0:
                    owner_name = self.outputOwnedBy(i + 1, player_names)
                    print(f"{i + 1}. {name} - Owned by {owner_name} - Price: ${price} - Rent: ${rent}")
                elif name in ["Go", "Tax", "Chance", "Jail", "Go to Jail"]:
                    print(f"{i + 1}. {name}")

    def printPropertyName(self,path): #test function
        with open(path, 'r') as file: #123
            lines = file.readlines()

            for i, line in enumerate(lines):
                name, price, rent = line.strip().split(',')
                rent = int(rent)

                if rent > 0:
                    print(f"{i+1}. {name}")

    def importGbfromFunc(self,path): #test
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

    def listDictToCommaDivided(self, listDict): #test
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

    def modifyGameboard(self):
        while True:
            backup = self.sqaures
            print("\nOptions:"
                  "1. Change property order"
                  "2. Change property name"
                  "3. Save and exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                print("\nCurrent order:")
                self.getProptertyList()
                try:
                    old_pos = input_number_within_range(1,20)
                    new_pos = input_number_within_range(1,20)
                    property = self.sqaures.pop(old_pos-1)
                    self.sqaures.insert(new_pos-1,property)
                    print("Property order updated.")
                except ValueError:
                    print("Invalid input. Please try again.")

            elif choice == "2":
                print("\nCurrent properties")
                self.getProptertyList()
                try:
                    pos = input_number_within_range(1, 20)
                    newName = input("Enter the new property name: ")
                    if double_confirm_true_false():
                        self.sqaures[pos-1]['name'] = newName
                        print("Property name updated.")
                    else:
                        print("No changes would be made")
                except ValueError:
                    print("Invalid input. Please try again.")

            elif choice == "3":
                if not self.validate_board_noTerminate(self.sqaures):
                    while True:
                        ch2 = input("Would you like to continue modifying(m) or exit without save(e)? ").strip().lower()
                        if ch2 == "m":
                            break
                        if ch2 == "e":
                            self.sqaures = backup
                            print("No changes would be saved")
                            return
                        else:
                            print("Invalid input. Please try again")
                            continue



    def validate_board(self, board_text):
        go_count = 0
        tax_count = 0
        jail_count = 0
        chance_count = 0
        gotojail_count = 0
        errors = []

        if len(board_text) != 20:
            errors.append(f"Error: The board data must have exactly 20 lines, but found {len(board_text)} lines.")

        for i, line in enumerate(board_text, start=1):
            if len(line) != 3:
                errors.append(f"Format error: Line {i} must have exactly 3 keys (name, price, rent).")
                continue

            name = line['name']
            price = line['price']
            rent = line['rent']

            if name == 'Go':
                go_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Go must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Tax':
                tax_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Tax must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Jail':
                jail_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Jail must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Chance':
                chance_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Chance must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Go To Jail':
                gotojail_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - GoToJail must have 0 for both price and rent, but got ({price}, {rent}).")

        if go_count != 1:
            errors.append(f"Error: There must be exactly one Go, but found {go_count}.")
        if tax_count < 1 or tax_count > 3:
            errors.append(f"Error: There must be between 1 and 3 Tax, but found {tax_count}.")
        if jail_count != 1:
            errors.append(f"Error: There must be exactly one Jail, but found {jail_count}.")
        if chance_count < 1 or chance_count > 3:
            errors.append(f"Error: There must be between 1 and 3 Chance, but found {chance_count}.")
        if gotojail_count < 1 or gotojail_count > 3:
            errors.append(f"Error: There must be between 1 and 3 GoToJail, but found {gotojail_count}.")

        if errors:
            for error in errors:
                print(error)
            raise SystemExit("Board data is not valid.")

        return True

    def validate_board_noTerminate(self, board_data):
        go_count = 0
        tax_count = 0
        jail_count = 0
        chance_count = 0
        gotojail_count = 0
        errors = []

        if len(board_data) != 20:
            errors.append(f"Error: The board data must have exactly 20 lines, but found {len(board_data)} lines.")

        for i, line in enumerate(board_data, start=1):
            if len(line) != 4:
                errors.append(f"Format error: Line {i} must have exactly 4 keys (name, isOwned, price, rent).")


            name = line['name']
            price = line['price']
            rent = line['rent']

            if name == 'Go':
                go_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Go must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Tax':
                tax_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Tax must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Jail':
                jail_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Jail must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Chance':
                chance_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - Chance must have 0 for both price and rent, but got ({price}, {rent}).")
            elif name == 'Go To Jail':
                gotojail_count += 1
                if price != 0 or rent != 0:
                    errors.append(
                        f"Error: Line {i} - GoToJail must have 0 for both price and rent, but got ({price}, {rent}).")

        if go_count != 1:
            errors.append(f"Error: There must be exactly one Go, but found {go_count}.")
        if tax_count < 1 or tax_count > 3:
            errors.append(f"Error: There must be between 1 and 3 Tax, but found {tax_count}.")
        if jail_count != 1:
            errors.append(f"Error: There must be exactly one Jail, but found {jail_count}.")
        if chance_count < 1 or chance_count > 3:
            errors.append(f"Error: There must be between 1 and 3 Chance, but found {chance_count}.")
        if gotojail_count < 1 or gotojail_count > 3:
            errors.append(f"Error: There must be between 1 and 3 GoToJail, but found {gotojail_count}.")

        if errors:
            for error in errors:
                print(error)
            print("Board data is not valid.")
            return False

        return True

    def getDefaultPath(self):
        return self.defaultpath

    def getPropertyName(self,position):
        position = int(position)
        return self.sqaures[position-1]["name"]

    def getPropertyPrice(self,posistion):
        position = int(posistion)
        return self.sqaures[posistion-1]["price"]

    def getPropertyRent(self,posistion):
        position = int(posistion)
        return self.sqaures[posistion-1]["rent"]


