import time
import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkinter import Text

from click import command
from wheel.macosx_libfile import swap32

from symulacja.classes.organizmy.zwierzeta.antylopa import Antylopa
from symulacja.classes.organizmy.zwierzeta.czlowiek import Czlowiek
from symulacja.classes.organizmy.zwierzeta.lis import Lis
from symulacja.classes.organizmy.zwierzeta.owca import Owca
from symulacja.classes.organizmy.zwierzeta.wilk import Wilk
from symulacja.classes.organizmy.zwierzeta.zolw import Zolw
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

        # -- Buttons --
        btn_tura = tk.Button(self.side_panel, text="Wykonaj Ture", command=self.wykonaj_ture)
        btn_save = tk.Button(self.side_panel, text="Zapisz", command=self.save_world)
        btn_load = tk.Button(self.side_panel, text="Wczytaj", command=self.load_world)
        btn_log_up = tk.Button(self.side_panel, text="^",command=lambda : self.przesun_log("DOWN"))
        btn_log_down = tk.Button(self.side_panel, text="v",command=lambda : self.przesun_log("UP"))
        btn_tura.pack()
        btn_save.pack()
        btn_load.pack()
        btn_log_up.pack()
        btn_log_down.pack()

        # -- Drop Down --
        # Dropdown
        self.selected_organizm = tk.StringVar()
        self.dropdown = ttk.Combobox(self.side_panel, textvariable=self.selected_organizm)
        self.dropdown['values'] = ["Wilk", "Owca", "Lis", "Zolw", "Antylopa", "Czlowiek"]
        self.dropdown.current(0)
        self.dropdown.pack()

        self.canvas_frame.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        # -- Bind click --
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Log window (tk.Text)
        self.log_window = Text(self.side_panel, height=20, state='disabled', wrap='word')
        self.log_window.pack(fill='both', expand=True, padx=5, pady=5)

        self.init_world()



    def init_world(self):
        if self.controller.settings.map_type == 'square':
            self.swiat = SwiatKwadratowy(self.canvas, self.log_window,self.controller.settings)
            self.load_world(self.lvl_path)
        elif self.controller.settings.map_type =='hex':
            self.swiat = SwiatHex(self.canvas, self.log_window)
        else:
            raise ValueError("Unknown map type selected.")

    def wykonaj_ture(self):
        self.swiat.wykonaj_ture()

    #zapisywanie swiata do pliku
    def save_world(self):
        self.swiat.save("files/save.txt")

    #ladowanie swiata z pliku i wyswietlanie go
    def load_world(self,file_path="files/save.txt"):
        self.swiat.load(file_path)
        self.swiat.sortuj_wszystkie()
        self.swiat.usun_zabite()
        self.swiat.organizmy.extend(self.swiat.nowe)
        self.swiat.nowe.clear()
        self.swiat.rysuj_swiat()
        self.swiat.wyswietl_logi(self.swiat.top_log)

    def on_canvas_click(self, event):
        cell_size = self.swiat.cell_size
        x = event.x // cell_size
        y = event.y // cell_size
        nazwa = self.selected_organizm.get()

        organizm = self.stworz_organizm(nazwa, x, y)
        if organizm:
            self.swiat.nowy_log(f"Dodano {nazwa} na ({x}, {y})")
            self.swiat.nowy_organizm(organizm)
            self.swiat.wykonaj_ture()

    def stworz_organizm(self, nazwa, x, y):
        mapping = {
            "Wilk": Wilk,
            "Owca": Owca,
            "Lis": Lis,
            "Zolw": Zolw,
            "Antylopa": Antylopa,
            "Czlowiek": Czlowiek
        }
        cls = mapping.get(nazwa)
        if cls:
            return cls(x, y, self.swiat)
        return None

    def przesun_log(self,direction):
        if direction == "UP":
            self.swiat.set_top_log_index(self.swiat.get_top_log_index() + 1)
        elif direction == "DOWN":
            self.swiat.set_top_log_index(self.swiat.get_top_log_index() - 1)
        else:
            print("ERROR: DIRECTION IS NOT CORRECT")