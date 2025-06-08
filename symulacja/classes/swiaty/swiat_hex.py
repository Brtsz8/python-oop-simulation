import tkinter as tk
import math
from symulacja.classes.swiat import Swiat

class SwiatHex(Swiat):
    def __init__(self, canvas, side_panel, settings):
        super().__init__(canvas, side_panel, settings)
        self.settings = settings
        self.color1 = "#aad751"
        self.color2 = "#a2d149"

    def rysuj_swiat(self):
        canvas = self.win
        canvas.delete("all")

        cols = self.settings.width
        rows = self.settings.height
        size = self.settings.cell_size  # Długość boku heksa

        hex_height = math.sqrt(3) * size
        hex_width = 2 * size
        vert_spacing = hex_height
        horiz_spacing = 3/4 * hex_width

        padding_x = 1/2 * hex_width
        padding_y = 1/2 * hex_height

        for row in range(rows):
            for col in range(cols):
                x = col * horiz_spacing + padding_x
                y = row * vert_spacing + padding_y

                if col % 2 == 1:
                    y += vert_spacing / 2  # przesunięcie co drugiej kolumny

                color = self.color1 if (col + row) % 2 == 0 else self.color2
                self._rysuj_hex(canvas, x, y, size, fill=color)

        # Rysowanie organizmów
        for organizm in self.organizmy:
            ox, oy = organizm.get_pozycja_x(), organizm.get_pozycja_y()

            x = ox * horiz_spacing + padding_x
            y = oy * vert_spacing + padding_y
            if ox % 2 == 1:
                y += vert_spacing / 2

            color = self.kolor_organizmu(organizm.nazwa())

            canvas.create_oval(
                x - size / 2 + 5,
                y - size / 2 + 5,
                x + size / 2 - 5,
                y + size / 2 - 5,
                fill=color,
                outline="black"
            )

    def _rysuj_hex(self, canvas, x, y, size, fill="white"):
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.radians(angle_deg)
            px = x + size * math.cos(angle_rad)
            py = y + size * math.sin(angle_rad)
            points.append(px)
            points.append(py)
        canvas.create_polygon(points, fill=fill, outline="black")

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
