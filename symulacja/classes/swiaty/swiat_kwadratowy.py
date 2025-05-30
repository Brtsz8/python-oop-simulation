import tkinter as tk

from symulacja.classes.swiat import Swiat

class SwiatKwadratowy(Swiat):
    def __init__(self, canvas, side_panel):
        super().__init__(canvas,side_panel)

    def rysuj_swiat(self):
        canvas = self.win
        canvas.delete("all")  # Clear previous drawings

        rows = 10
        cols = 10
        cell_size = 40

        # Draw checkered grid
        for y in range(rows):
            for x in range(cols):
                color = "#aad751" if (x + y) % 2 == 0 else "#a2d149"
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
            "Wilcze Jagody": "darkblue",
            "Barszcz Sosnowskiego": "darkgreen",
        }
        return colors.get(nazwa, "black")