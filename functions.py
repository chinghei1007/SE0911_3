import configparser
import os.path
import random
import tkinter as tk
from tkinter import filedialog


def drawDice():
    return random.randint(1, 6)

def developerMode():
    while True:
        print("What do you want?")
        print("1. Import gameboard")
        print("2. Export gameboard")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            importGbFunc()
            print("Gameboard imported.")
        elif choice == '2':
            # Export gameboard code here
            print("Gameboard exported.")
        elif choice == '3':
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

def importGbFunc():
    while True:
        root = tk.Tk()
        root.withdraw

        path = filedialog.askopenfilename(
            title = "Please select the txt file containing Gameboard",
            filetypes = (("Text files", ".py"), ("All files", "*.*"))
        )

        if path:
            print(f"Selected file: {path}")
            choice = input("Would you like to set as default path? y/n").strip().lower()
            if choice == 'y':
                saveDefaultPath(path)
            if choice == 'n':
                print(f"Default path hasn't changed: {getDefaultPath()}")
            from gameboard import Gameboard as gb
            gb.importGbfromFunc(path)


def getDefaultPath():
    config = configparser.ConfigParser()
    file = "config.ini"

    if os.path.exists(file):
        config.read(file)
        if "DEFAULT" in config and "path" in config["DEFAULT"]:
            return config["DEFAULT"]["path"]
    else:
        config["DEFAULT"] = {"path":"./property.txt"}
        with open(file, "w") as f:
            config.write(f)
            return "./property.txt"

def saveDefaultPath(path):
    config = configparser.ConfigParser()
    config.read("config.ini")
    config["DEFAULT"]["path"] = path
    with open("config.ini", "w") as f:
        config.write(f)
    print("Default Path set")