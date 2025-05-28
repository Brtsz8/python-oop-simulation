import tkinter as tk
from tkinter import Frame

class WorldSelectionView(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller =controller
        self.pack()

        label = tk.Label(self, text="Wybierz typ świata:")
        label.pack()

        btn1 = tk.Button(self, text="Świat Kwadratowy", command=self.select_square)
        btn2 = tk.Button(self, text="Świat Hex", command=self.select_hex)
        btn1.pack()
        btn2.pack()

    def select_square(self):
        self.controller.settings.set_map_sqr()
        #self.controller.show_level_selection()

    def select_hex(self):
        self.controller.settings.set_map_hex()
        #self.controller.show_level_selection()