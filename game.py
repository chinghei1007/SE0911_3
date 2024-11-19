import gameboard as gb
import functions
from character import Character
from instructions import *

player_names = []
def buyOrPayRent(player, sqaure, position, gameboard):
    IDandRent = [0, -1]
    print("buyOrPayRent has been run")
    name = gameboard.getPropertyName(position)
    price = gameboard.getPropertyPrice(position)
    rent = gameboard.getPropertyRent(position)
    print(f"\nProperty information: {name}"
          f" Price: {price}"
          f" Rent: {rent}")
    if not (gameboard.IsOwned(position)):
        while (True):
            value = input(f"Would you like to Buy (B) or Pass (P) {name}?: ").lower()
            match value:
                case "b":
                    buyProperty(name, position, player, gameboard)
                    return IDandRent
                case "p":
                    print("No changes would be made")
                    return IDandRent
                case _:
                    "Invalid input, please try again"

    else:
        IDandRent = payRent(name, position, player, gameboard)
        return IDandRent

def buyProperty(name, position, player, gameboard):
    propertyPrice = gameboard.getPropertyPrice(position)
    if player.coins >= propertyPrice:
        player.property.append(name)
        player.coins -= propertyPrice
        ID = getPlayerID(player.name)
        gameboard.activateOwned(position, ID)
        print(f"You now have {player.coins} left")
    else:
        print(f"You need {propertyPrice} but you only have {player.coins}. You couldn't buy the property. No changes were made")

def payRent(name, position, player ,gameboard):
    IDandRent = [0,-1]
    propertyRent = gameboard.getPropertyRent(position)
    propertyOwned = gameboard.OwnedbyID(position)
    if propertyRent > player.coins:
        player.retire = True
        print(f"Insufficient balance to pay rent {propertyRent}, you will now be retired")
    else:
        player.coins -= propertyRent
        IDandRent = [propertyOwned,propertyRent]
        print(f"{propertyRent} were charged, You now have {player.coins} left")

    return IDandRent

def draw_then_position_change(player, gameboard):
    step1 = functions.drawDice()
    step2 = functions.drawDice()
    #holding for pay rent
    payRentandID = [0,-1]
    print(f"You drawed {step1} and {step2}")
    # Check In jail rounds
    if player.in_jail_round == 3:
        player.go_retire()
        # If in jail, don't move
    elif player.in_jail:
        player.in_jail_round += 1
        print(f"You didn't draw double, you are in jail for {player.in_jail_round} rounds")
        # If in jail and double dice, move
    elif player.in_jail & step1 == step2:
        player.releaseFromJail(step1 + step2)
        print("You have drawn a double, you are now released")
        if player.position > 20:
            player.position -= 20
            print(f"Your position is now {player.position}")
            payRentandID = special_square(player, player.getPropertyType(character.position), player.position,
                                          gameboard)
            # print(f"Test get PropertyType: {player.getPropertyType(player.position)} at {player.position}")
        else:
            print(f"Your position is now {player.position}")
            # print(f"Test get PropertyType: {player.getPropertyType(player.position)} at {player.position}")
            payRentandID = special_square(player, player.getPropertyType(character.position), player.position,
                                          gameboard)
        # character.special_square(character.getPropertyName(character.position))
        input("Press enter to continue")
        return payRentandID
    else:
        # change position, then determine propter type, pass to special square

        player.position += step1 + step2
        if player.position > 20:
            player.position -= 20
            print(f"Your position is now {player.position}")
            payRentandID = special_square(player, player.getPropertyType(character.position), player.position, gameboard)
            #print(f"Test get PropertyType: {player.getPropertyType(player.position)} at {player.position}")
        else:
            print(f"Your position is now {player.position}")
            #print(f"Test get PropertyType: {player.getPropertyType(player.position)} at {player.position}")
            payRentandID = special_square(player, player.getPropertyType(character.position), player.position, gameboard)
        # character.special_square(character.getPropertyName(character.position))
    input("Press enter to continue")
    return payRentandID




def special_square(player, sqare, position, gameboard):
    print(f"Test special_sqaure has been run, {sqare}")
    payRentandID = [0, -1]
    match sqare:
        case "Property":
            payRentandID = buyOrPayRent(player, sqare, position, gameboard)  # prompt user to choose buy or pay
            return payRentandID
        case "Go":  # coin +1500
            player.coin_change(1500)
            print("Blance changed +1500")
            print(f"You now have ${player.coins}")
            return payRentandID
        case "Chance":  # coin +200 to -300
            change = (random.randint(-30, 20) * 10)
            player.coin_change(change)
            print(f"Balance changed {change}")
            print(f"You now have ${player.coins} left")
            return payRentandID
        case "Tax":
            player.coin_change(-int(player.coins * 0.1))
            print(f"You now have {player.coins} left")
            return payRentandID
        case "Free Parking":
            print("You've got Free Parking, no changes to your status")
            return payRentandID
        case "Go To Jail":
            player.go_to_jail()
            return payRentandID
        case "Jail":
            if not player.in_jail: print("No changes would be made")
            return payRentandID
            # 7 kinds of square

def getIfPropertyIsOwned(sqaure, position):
    pass

def print_player_positions_with_balance(user):
    print("\nPositions and balance of players:")
    positions = [f"{player.getName()}: {player.getPosition()}, Balance: {player.coins}" for player in user]
    print(", ".join(positions))

def getPlayerID(name):
    return player_names.index(name)

# Start
rounds = 0

while True:
    gameboard = gb.Gameboard()
    completemap = gameboard.setup_board()  # returns list of dictionaries with properties information

    dev = input("Are you a developer? y/n: ").strip().lower()
    if dev == 'y':
        print("Now will take you to game setup")
        functions.developerMode(gameboard)
    elif dev == 'n':
        print("Now will take you to the game")
    else:
        print("invalid input, please try again")
        continue

    player_count = get_number_of_players()
    player_names = get_player_names(player_count)
    player_names_in_game = player_names
    user = [Character(name) for name in player_names]

    print("You now have players as ")
    for i, character in enumerate(user):
        print(f"Player {i + 1}: {character.getName()}")

    print("\n\nThe Game will now start")

    while rounds <= 100 and len(player_names_in_game) > 1:
        for character in user:
            print(f"\n\nRound {rounds + 1}")

            #print property informations and player posistion
            gameboard.printPropertyNamewithOwned(player_names)
            print_player_positions_with_balance(user)

            rentandID = [0,-1]
            if not character.IsRetired():
                print(f"\n{character.getName()}'s turn:")
                input("Press Enter to roll the dice")
                rentandID = draw_then_position_change(character, gameboard)
                rent, ID = rentandID
                if ID > 0:
                    user[ID].coins += rent

        rounds += 1

        # Check for retired players
        player_names_in_game = [player.getName() for player in user if not player.IsRetired()]

        if len(player_names_in_game) == 1:
            print(f"Congratulations, {player_names_in_game[0]} has won the game!")
            break

    if input("Do you want to play again? (y/n)").lower().strip() != 'y':
        break



