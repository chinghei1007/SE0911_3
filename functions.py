import configparser
import os.path
import random
import tkinter as tk
from tkinter import filedialog


def drawDice():
    return random.randint(1, 4) #4 faced dice

def developerMode(o):
    while True:
        print("What do you want?")
        print("1. Import gameboard")
        print("2. Export gameboard")
        print("3. Modify Gameboard")
        print("4. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            path = importGbFunc()
            if path:
                print("Gameboard imported.\n")
                o.reinitializeBoard(path)
        elif choice == '2':
            exportGbFunc(o)
        elif choice == '3':
            modifyGb(o)
        elif choice == '4':
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

def modifyGb(o):
    o.modifyGameboard()

def importGbFunc():
    root = tk.Tk()
    file_path = filedialog.askopenfilename(title="Browse File", filetypes=[("Text files", "*.txt")])
    root.destroy()
    return file_path

def exportGbFunc(o):
    current = o.getProptertyList()
    toText = ""
    for dict in current:
        toText += f"{dict['name']},{dict['price']},{dict['rent']}\n"

    root = tk.Tk
    root.title("Choose your save location")
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if path:
        with open(path, 'w') as file:
            file.write(toText)
        print(f"Gameboard exported to: {path}")
    else:
        print("Export cancelled.")

    root.destroy()

def getDefaultPath():
    config = configparser.ConfigParser()
    file = "config.ini"

    if os.path.exists(file):

        config.read(file)
        if "DEFAULT" in config and "path" in config["DEFAULT"]:
            #print(config["DEFAULT"]["path"])
            return config["DEFAULT"]["path"]
        else:
            print("Now will set the default path")
            config["DEFAULT"] = {"path":"property.txt"}
            with open(file, "w") as f:
                config.write(f)
                return "property.txt"

def saveDefaultPath(path):
    config = configparser.ConfigParser()
    config.read("config.ini")
    config["DEFAULT"]["path"] = path
    with open("config.ini", "w") as f:
        config.write(f)
    print("Default Path set")