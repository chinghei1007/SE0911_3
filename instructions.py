import random

#0920: get player names > change player names
#print player names, inputNumberWithinRange, draw, doubleConfirm
def get_number_of_players():
    while True:
        print("Please input the number of players")
        players = input_number_within_range(2,6)
        confirm = input(f"You entered {players}. Confirm? (y/n)").strip().lower()
        if confirm == 'y': print(f"Number of players set to: {players}"); return players
        else: print('Please enter the number of players again.')

def get_player_names(num_players):
    #collect names
    player_names = []
    for i in range(num_players):
        name = input(f"Enter name of player {i+1}: ")
        player_names.append(name)

    #confirm or edit names
    while True:
        print_player_names(player_names)
        choice = input("Do you want to confirm the names or edit them? (c to confirm, e to edit)").strip().lower()
        match choice:
            case 'c':
                return player_names
            case 'e':
                player_names = change_player_names(player_names);break
            case _ :
                print("Invalid input, try again")

def change_player_names(player_names):
    original_names = player_names.copy()

    while True:
        print("\n Current player names:")
        print_player_names(player_names)
        print("\nPlease input the player number that you want to change the name of (0 to finish editing)")
        choice = input_number_within_range(0,len(player_names))
        if choice == 0: break
        if 1 <= choice <= len(player_names):
            new_name = input(f"Enter a new name for player {choice} (current: {player_names[choice - 1]}): ").strip()
            if new_name:
                player_names[choice - 1] = new_name
            else:
                print("Invalid range, try again")

    #Confirm changes
    print("\nUpdated player names:")
    print_player_names(player_names)
    while True:
        print(
        "\nIt is recommened to change the name again in case you typed the wrong name, choosing n will revert ALL changes")
        confirm = input("Do you want to save these changes? (y to save, n to revert, c to continue editing)")
        match confirm:
            case 'y':
                print("Changes saved");return player_names
            case 'n':
                print("ALL of the changes will be reverted")
                d_confirm = double_confirm()
                if d_confirm == 'y': player_names = original_names; return player_names;
                if d_confirm == 'n': continue
            case 'c':
                return change_player_names(player_names);
            case _:
                print("Input invalid, try again")
                continue

def print_player_names(player_names):
    if len(player_names) > 0:
        for i, name in enumerate(player_names, start=1):
            print(f"Player {i} : {name}")

def draw():
    return (random.randint(1,6),random.randint(1,6))

def read_to_list(path): #input text file, designer 要改東西就入去改
    list = []
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                #print(i)
                divided = line.strip().split(',')
                #print(divided)
                list.append({
                    "name": divided[0].strip(),
                    "price": int(divided[1].strip()),
                    "rent": int(divided[2].strip())
                })
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"Error {e}")

    return list

def input_number_within_range(min,max):
    while True:
        try:
            number = int(input())
            if min<=number<=max:
                return number
            else:
                print(f"Error: the number must be between {min} and {max}. Please try again")
        except ValueError:
            print("Please enter a valid number. ")

def double_confirm():
    while True:
        choice = input("Are you sure? (y/n)")
        match choice:
            case 'y':
                return 'y'
            case 'n':
                return 'n'
            case _:
                print("Please type only y or n")
                continue
