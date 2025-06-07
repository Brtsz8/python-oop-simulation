import tkinter as tk

from symulacja.classes.swiat import Swiat

class SwiatKwadratowy(Swiat):
    def __init__(self, canvas, side_panel,settings):
        super().__init__(canvas,side_panel,settings)
        self.settings = settings
        #kolory planszy
        self.color1 = "#aad751"
        self.color2 = "#a2d149"

    #funkjca nadpisuje klase swiat
    #jedna z dwoch podklas kwadrat/hex
    # - informacje takie jak rows/cols/cell_size wczytywane przez klase settings
    # - kolory planszy inicjalizowane wraz z klasa (w przyszlosci mozna wprowadzic wczytywanie z pliku)
    def rysuj_swiat(self):
        canvas = self.win
        canvas.delete("all")  #czyszczenie tego co bylo wczesniej

        #wczytywanie ustawien
        cols = self.settings.width
        rows = self.settings.height
        cell_size = self.settings.cell_size

        # Draw checkered grid
        for y in range(rows):
            for x in range(cols):
                color = self.color1 if (x + y) % 2 == 0 else self.color2
                canvas.create_rectangle(
                    x * cell_size,
                    y * cell_size,
                    (x + 1) * cell_size,
                    (y + 1) * cell_size,
                    fill=color,
                    outline="black"
                )

        # Draw organisms
        for organizm in self.organizmy:
            ox, oy = organizm.get_pozycja_x(), organizm.get_pozycja_y()
            color = self.kolor_organizmu(organizm.nazwa())

            canvas.create_oval(
                ox * cell_size + 5,
                oy * cell_size + 5,
                (ox + 1) * cell_size - 5,
                (oy + 1) * cell_size - 5,
                fill=color,
                outline="black"
            )
        #log for testing
        #print("koniec rysowania")

    def kolor_organizmu(self, nazwa):
        colors = {
            "Wilk": "gray",
            "Owca": "white",
            "Lis": "orange",
            "Zolw": "green",
            "Antylopa": "tan",
            "Czlowiek": "blue",
            "Cyberowca": "purple",
            "Trawa": "lightgreen",
            "Mlecz": "yellow",
            "Guarana": "red",
            "Wilcze_Jagody": "darkblue",
            "Barszcz_Sosnowskiego": "darkgreen",
        }
        return colors.get(nazwa, "black")