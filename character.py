import functions
import instructions as inst
import gameboard as gb
import random
#1
player_count = 0
a = gb.Gameboard()
a.setup_board()
list = a.getProptertyList()

defaultpropertycost = (-1,800,700,-1,600,-1,400,500,-1,400,-1,700,-1,400,500,-1,400,400,-1,600)
class Character():
    def __init__(self, name):
        self.coins = 1500
        self.property = []
        self.name = name
        self.position = 1
        self.in_jail = False
        self.in_jail_round = 0
        self.salary = 0
        self.taxes = 0
        self.fines = 0
        self.retire = False

    def __str__(self):
        return self.name

    def coin_change(self,coin):
        self.coins += coin
        if self.coins < 0:
            self.retire = True
            self.property = []

    def getPropertyRent(self,position):
        gpt = gb.Gameboard()
        gpt.setup_board()
        list = gpt.getProptertyList
        property_rent = list[position - 1]["rent"]
        print("getPropertyRent has run")
        return property_rent

    def getPropertyPrice(self,position):
        gpt = gb.Gameboard()
        gpt.setup_board()
        list = gpt.getProptertyList
        property_price = list[position - 1]["price"]
        print("getPropertyPrice has run")
        return property_price

    def getPropertyName(self,position):
        gpt = gb.Gameboard()
        gpt.setup_board()
        list = gpt.getProptertyList
        property_name = list[position - 1]["name"]
        print("getPropertyName has run")
        return property_name

    def getPropertyType(self,position):
        gpt = gb.Gameboard()
        gpt.setup_board()
        list = gpt.getProptertyList()
        #print(len(list))
        #result = ["Property" if item["rent"] > 0 else item["name"] for item in list]
        item = list[position-1]
        if item["rent"] > 0:
            return "Property"
        else:
            return item["name"]

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getOwnedProperties(self):
        return self.property

    def getCoins(self):
        return self.coins

    def getStatus(self):
        return self.in_jail, self.in_jail_round #要改

    def go_to_jail(self):
        jail_index = next((i for i, d in enumerate(list) if d["name"] == "Jail"), -1)
        self.position = jail_index+1 #find jail position
        self.in_jail = True
        # when in jail, round ++

    def releaseFromJail(self,steps):
        self.in_jail = False
        self.in_jail_round = 0
        self.position += steps

    def IsRetired(self):
        return self.retire
    def isRetired(self):
        return self.retire

    def go_retire(self):
        self.retire = True

    def position_change(self,step1, step2):
        # Check In jail rounds
        if self.in_jail_round == 3:
            self.go_retire()
        # If in jail, don't move
        elif self.in_jail:
            self.in_jail_round += 1
        # If in jail and double dice, move
        elif self.in_jail & step1==step2:
            self.releaseFromJail(step1+step2)
        else:
            #change position, then determine propter type, pass to special square
            self.position += step1+step2

            if self.position > 20:
                self.position -=20

        return self.coins, self.position

    def switchToJail(self): #testPurpose
        if self.in_jail == True: return
        self.in_jail = True

"""p1 = character("Tom")
price = p1.getPropertyPrice(3)
proper = p1.getPropertyName(3)
print(f"{p1.getName()} will buy {proper} for {price}")"""