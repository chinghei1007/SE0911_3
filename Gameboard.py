import instructions as inst
class GameBoard:
    def __init__(self):
        self.sqaures = inst.read_to_list("prop.txt") #[{name}{price}{rent}]


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

    def printProperty(self,path): #test function
        with open(path, 'r') as file:
            lines = file.readlines()

            for i, line in enumerate(lines):
                name, price, rent = line.strip().split(',')
                rent = int(rent)

                if rent > 0:
                    print(f"{i+1}. {name}")
