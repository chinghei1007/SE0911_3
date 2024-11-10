import functions
import instructions as inst
import random
import Game as G

player_count = 0
propertiesdict = {
    'Go' : 0, #should not be changed
    'Central' : 800,
    'Wan Chai' : 700,
    'Income Tax' : -10,
    'Stanley' : 600,
    'Jail' : 0,
    'Shek O' : 400,
    'Mong Kok' : 500,
    '? Chance' : 0,
    'Tsing Yi' : 400,
    'Free Parking' : 0,
    'Shatin' : 700,
    '? Chance' : 0,
    'Tuen Mun' : 400,
    'Tai Po' : 500,
    'Go to Jail' : 0,
    'Sai Kung' : 400,
    'Yuen Long': 400,
    '? Chance': 0,
    'Tai O': 600

}

defaultpropertycost = (-1,800,700,-1,600,-1,400,500,-1,400,-1,700,-1,400,500,-1,400,400,-1,600)
class character():
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

    def draw_then_position_change(self):
        step1 = functions.drawDice()
        step2 = functions.drawDice()
        # If in jail, don't move
        if self.in_jail & step1==step2: #in jail and double throw
            self.releaseFromJail(step1+step2)
        else:
            self.position += step1+step2
            if self.position > 20:
                self.position -=20
                self.special_square("Go") #+1500 coins

    def special_square(self,sqare):
        match sqare:
            case "Property":
                self.buyOrPayRent(sqare) #prompt user to choose buy or pay
            case "Go": #coin +1500
                self.coin_change(1500)
            case "Chance": #coin +200 to -300
                self.coin_change(random.randint(-30, 20) * 10)
            case "Income Tax":
                self.coin_change(-int(self.coins * 0.1))
            case "Free Parking":
                print("You've got Free Parking")
            case "Go to Jail":
                self.go_to_jail()
            #7 kinds of square


    def coin_change(self,coin):
        self.coins += coin
        if self.coins < 0:
            self.retire = True
            self.property = []

    def buyOrPayRent(self,sqare):
        propertyname = G.completemap[self.position]['name']

        if (G.completemap[self.position]['owned'] == -1):
            value = input(f"Would you like to Buy (B) or Pass (P) {propertyname}?").lower().strip()
            while (True):
                match value:
                    case "b":
                        self.buyPropertyNoRent()
                        return
                    case "p":
                        return
                    case _:
                        "Invalid input, please try again"

        else:
            value = input(f"Would you like to Buy (B) or pay Rent(R) to {sqare}?").lower().strip()
            while(True):

                match value:
                    case "b":
                        self.buyProperty()
                        return
                    case "r":
                        self.payRent()
                        return
                    case _:
                        "Invalid input, please try again"

    def buyProperty(self):
        prop = inst.read_to_list("prop.txt")
        propertyPrice = prop[self.position-1]['price']
        if self.coins >= propertyPrice:
            self.property.append(prop[self.position-1]['name'])
            self.coins -= propertyPrice
        else:
            print("Insufficient balance, you are now forced to pay rent")
            self.payRent()

    def buyPropertyNoRent(self):
        prop = inst.read_to_list("prop.txt")
        propertyPrice = prop[self.position-1]['price']
        if self.coins >= propertyPrice:
            self.property.append(prop[self.position-1]['name'])
            self.coins -= propertyPrice
        else:
            print("Insufficient balance, no action done.")

    def payRent(self):
        prop = inst.read_to_list("prop.txt")
        propertyRent = prop[self.position-1]['rent']
        if propertyRent > self.coins:
            self.retire = True
        else:
            self.coins -= propertyRent
            print(f"{propertyRent} were charged, You now have {self.coins} left")

    def getPropertyPrice(self,position):
        property_name = self.getPropertyName(position)
        return propertiesdict.get(property_name,1)

    def getPropertyName(self,position):
        list_properties = list(propertiesdict.keys())
        return list_properties[position - 1]

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getOwnedProperties(self):
        return self.property

    def getStatus(self):
        return self.in_jail, self.in_jail_round #要改

    def go_to_jail(self):
        key = list(propertiesdict.keys())
        print(key.index("Jail"))
        self.position = key.index("Jail")+1 #find jail position
        self.in_jail = True
        # when in jail, round ++

    def releaseFromJail(self,steps):
        self.in_jail = False
        self.position += steps

"""p1 = character("Tom")
price = p1.getPropertyPrice(3)
proper = p1.getPropertyName(3)
print(f"{p1.getName()} will buy {proper} for {price}")"""