import tkinter as tk
from tkinter import Frame

class LvlSelectionView(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller =controller
        self.pack()

        label = tk.Label(self, text="Wybierz Poziom:")
        label.pack()

        if self.controller.settings.map_type == 'square':
            self.show_sqr_lvl()
        else:
            self.show_hex_lvl()

    def show_sqr_lvl(self):
        lvl1 = tk.Button(self, text="Poziom 1", command=lambda: self.set_lvl('sqr',1))
        lvl2 = tk.Button(self, text="Poziom 2", command=lambda: self.set_lvl('sqr',2))
        lvlE = tk.Button(self, text="Poziom Pusty", command=lambda: self.set_lvl('sqr',0)) #0 bedzie odpowiadac za pusty poziom
        lvl1.pack()
        lvl2.pack()
        lvlE.pack()

    def show_hex_lvl(self):
        lvl1 = tk.Button(self, text="Poziom 1", command=lambda: self.set_lvl('hex',1))
        lvl2 = tk.Button(self, text="Poziom 2", command=lambda: self.set_lvl('hex',2))
        lvlE = tk.Button(self, text="Poziom Pusty", command=lambda: self.set_lvl('hex',0)) #0 bedzie odpowiadac za pusty poziom
        lvl1.pack()
        lvl2.pack()
        lvlE.pack()

    def set_lvl(self, type ,lvl):
        if type == 'sqr':
            self.controller.settings.set_lvl('s'+str(lvl))
        if type == 'hex':
            self.controller.settings.set_lvl('h'+str(lvl))
        self.controller.start_game()