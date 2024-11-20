import tkinter as tk
from tkinter import ttk

class MonopolyUI:
    def __init__(self, master, characters):
        self.master = master
        master.title("Monopoly")
        self.characters = characters

        # Create the main frame
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(padx=20, pady=20)

        # Create the round label
        self.round_label = ttk.Label(self.main_frame, text="Round x")
        self.round_label.grid(row=0, column=0, columnspan=6, pady=10)

        # Create the player label
        self.player_label = ttk.Label(self.main_frame, text=" ".join(f"P{i+1}:{character.getName()}" for i, character in enumerate(self.characters)))
        self.player_label.grid(row=1, column=0, columnspan=6, pady=10)

        # Create the property table
        self.property_table = ttk.Treeview(self.main_frame, columns=("Name", "Price", "Rent", "Owned"), show="headings")
        self.property_table.heading("Name", text="Name")
        self.property_table.heading("Price", text="Price")
        self.property_table.heading("Rent", text="Rent")
        self.property_table.heading("Owned", text="Owned")
        self.property_table.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

        # Create the player position labels
        self.player_position_labels = []
        for character in self.characters:
            label = ttk.Label(self.main_frame, text=f"{character.getName()} Position {character.getPosition()}")
            self.player_position_labels.append(label)
            label.grid(row=3+len(self.player_position_labels), column=0, columnspan=6, pady=5)

    def update_ui(self, round_number, player_names, property_list):
        self.round_label.config(text=f"Round {round_number}")
        self.player_label.config(text=" ".join(f"P{i+1}:{name}" for i, name in enumerate(player_names)))

        self.property_table.delete(*self.property_table.get_children())
        for property in property_list:
            self.property_table.insert("", "end", values=(property["name"], property["price"], property["rent"], property["owned"]))

        for i, label in enumerate(self.player_position_labels):
            label.config(text=f"{self.characters[i].getName()} Position {self.characters[i].getPosition()}")