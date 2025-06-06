import time
import tkinter as tk
from tkinter import Frame
from tkinter import Text

from symulacja.classes.organizmy.zwierzeta.owca import Owca
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

        btn1 = tk.Button(self.side_panel, text="Wykonaj Ture", command=self.wykonaj_ture)
        #to do
        btn2 = tk.Button(self.side_panel, text="Zapisz", command=self.save_world)
        btn3 = tk.Button(self.side_panel, text="Wczytaj", command=self.load_world)
        btn1.pack()
        btn2.pack()
        btn3.pack()

        self.canvas_frame.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Log window (tk.Text)
        self.log_window = Text(self.side_panel, height=20, state='disabled', wrap='word')
        self.log_window.pack(fill='both', expand=True, padx=5, pady=5)

        self.init_world()



    def init_world(self):
        if self.controller.settings.map_type == 'square':
            self.swiat = SwiatKwadratowy(self.canvas, self.log_window,self.controller.settings)
            self.swiat.nowy_organizm(Owca(1,1,self.swiat))
            self.swiat.nowy_organizm(Owca(1,2,self.swiat))
            self.swiat.wykonaj_ture()
        elif self.controller.settings.map_type =='hex':
            self.swiat = SwiatHex(self.canvas, self.log_window)
        else:
            raise ValueError("Unknown map type selected.")

    def wykonaj_ture(self):
        self.swiat.wykonaj_ture()

    def save_world(self):
        self.swiat.save("files/save.txt")

    def load_world(self):
        self.swiat.load("files/save.txt")
        self.swiat.sortuj_wszystkie()
        self.swiat.usun_zabite()
        self.swiat.organizmy.extend(self.swiat.nowe)
        self.swiat.nowe.clear()
        self.swiat.rysuj_swiat()
        self.swiat.wyswietl_logi(self.swiat.top_log)