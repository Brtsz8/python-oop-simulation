import tkinter as tk
from tkinter import Frame

from symulacja.classes.swiaty.swiat_hex import SwiatHex
from symulacja.classes.swiaty.swiat_kwadratowy import SwiatKwadratowy


class SimView(Frame):
    def __init__(self, parent, controller,lvl_path):
        super().__init__(parent)
        self.parent = parent
        self.controller =controller
        self.lvl_path = lvl_path
        self.swiat = None
        self.pack()

        if controller.setting.map_type == 'square':
            self.swiat = SwiatKwadratowy
        elif controller.setting.map_type =='hex':
            self.swiat = SwiatHex
