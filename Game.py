import Gameboard as gb
import chracter as cha
from instructions import *

#Start
rounds = 0

while True:
    playerCount = get_number_of_players()
    #output: set to n players
    playerNames = get_player_names(playerCount) #pN = list, leaderBoard
    playerNamesInGame = playerNames #retire, foul
    characters = [cha.character(name) for name in playerNames] #character class
    print("You now have players as ")
    for i in range(len(characters)):
        print(f"Player {i}: {characters[i].getName()}")

    o = gb.GameBoard()
    completemap = o.setup_board() #returns list of dictionaries with properties information
    print("\n\nThe Game will now start")
    #start

    while (rounds <= 100 and len(playerNamesInGame) > 1):
        print(f"\n\nRound {rounds}")
        print("\n\n")
        o.printProperty("property.txt")
        round =+ 1


