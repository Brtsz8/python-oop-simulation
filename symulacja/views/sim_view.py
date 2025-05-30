import tkinter as tk
from tkinter import Frame
from tkinter import Text

from symulacja.classes.swiaty.swiat_hex import SwiatHex
from symulacja.classes.swiaty.swiat_kwadratowy import SwiatKwadratowy


class SimView(Frame):
    def __init__(self, parent, controller,lvl_path,canvas_frame,side_panel):
        super().__init__(parent)
        self.parent = parent
        self.controller =controller
        self.lvl_path = lvl_path
        self.canvas_frame = canvas_frame
        self.side_panel = side_panel
        self.swiat = None
        self.pack()


        # Log window (tk.Text)
        self.log_window = Text(self.side_panel, height=20, state='disabled', wrap='word')
        self.log_window.pack(fill='both', expand=True, padx=5, pady=5)

        self.init_world()



    def init_world(self):
        if self.controller.settings.map_type == 'square':
            self.swiat = SwiatKwadratowy(self.canvas_frame, self.log_window)
            self.swiat.nowy_log("Wyswietl ten log pls")
            self.swiat.nowy_log("1 Wyswietl ten log pls")
            self.swiat.nowy_log("2 Wyswietl ten log pls")
            self.swiat.wykonaj_ture()
        elif self.controller.settings.map_type =='hex':
            self.swiat = SwiatHex(self.canvas_frame, self.side_panel)
        else:
            raise ValueError("Unknown map type selected.")