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

    def get_dirs(self, x = None):
        if x % 2 == 0:
            return [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, 1), (1, 1)]
        else:
            return [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (1, -1)]

    def get_deltas(self, x: int, y: int) -> list[tuple[int, int]]:
        if x % 2 == 0:
            return [
                (x - 1, y), (x + 1, y),
                (x, y - 1), (x, y + 1),
                (x - 1, y + 1), (x + 1, y + 1),
            ]
        else:
            return [
                (x - 1, y), (x + 1, y),
                (x, y - 1), (x, y + 1),
                (x - 1, y - 1), (x + 1, y - 1),
            ]
    def cube_to_oddq(self,x, z):
        col = x
        row = z + (x - (x & 1)) // 2
        return col, row

    def pixel_to_hex(self,x, y, size):
        # Pointy-topped hex layout — odd-q offset
        width = 3 / 2 * size
        height = math.sqrt(3) * size

        q = (x * 2 / 3) / size
        r = (-x / 3 + math.sqrt(3) / 3 * y) / size

        return self.cube_round(q, r, -q - r)

    def cube_round(self,x, y, z):
        rx = round(x)
        ry = round(y)
        rz = round(z)

        dx = abs(rx - x)
        dy = abs(ry - y)
        dz = abs(rz - z)

        if dx > dy and dx > dz:
            rx = -ry - rz
        elif dy > dz:
            ry = -rx - rz
        else:
            rz = -rx - ry

        return self.cube_to_oddq(rx, rz)


