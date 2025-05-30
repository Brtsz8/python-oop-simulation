import tkinter as tk

from symulacja.classes.swiat import Swiat

class SwiatHex(Swiat):
    def __init__(self, canvas_frame, side_panel):
        super().__init__(canvas_frame, side_panel)
        label = tk.Label(canvas_frame, text="Świat Hex", bg='lightblue')
        label.pack(expand=True, fill='both')

    def rysuj_swiat(self):
        print("swiat")