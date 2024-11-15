import gameboard as gb

import functions
from character import Character
from instructions import *

#Start
rounds = 0

while True:
    dev = input("Are you a developer? y/n").strip().lower()
    if dev == 'y':
            functions.developerMode()
    elif dev == 'n':
        print("okay")
    else:
        print("invalid input, please try again")
        continue

    playerCount = get_number_of_players()
    #output: set to n players
    playerNames = get_player_names(playerCount) #pN = list, leaderBoard
    playerNamesInGame = playerNames #retire, foul
    characters = [Character(name) for name in playerNames] #character class
    print("You now have players as ")
    for i in range(len(characters)):
        print(f"Player {i}: {characters[i].getName()}")

    o = gb.Gameboard()
    completemap = o.setup_board() #returns list of dictionaries with properties information
    print("\n\nThe Game will now start")
    #start

    while (rounds <= 100 and len(playerNamesInGame) > 1):
        print(f"\n\nRound {rounds}")
        print("\n\n")
        o.printProperty("property.txt")
        round =+ 1


