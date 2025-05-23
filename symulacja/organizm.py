import random
from typing import Tuple

class Organizm:
    def __init__(self, sila: int, inicjatywa: int, pozycja_x: int, pozycja_y: int, swiat):
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.pozycja_x = pozycja_x
        self.pozycja_y = pozycja_y
        self.swiat = swiat
        self.zyje = True

    # --- Getters ---
    def get_sila(self) -> int:
        return self.sila

    def get_inicjatywa(self) -> int:
        return self.inicjatywa

    def get_pozycja_x(self) -> int:
        return self.pozycja_x

    def get_pozycja_y(self) -> int:
        return self.pozycja_y

    def get_swiat(self):
        return self.swiat

    def get_zyje(self) -> bool:
        return self.zyje

    # --- Setters ---
    def set_sila(self, sila: int):
        self.sila = sila

    def set_inicjatywa(self, inicjatywa: int):
        self.inicjatywa = inicjatywa

    def set_pozycja(self, x: int, y: int):
        self.pozycja_x = x
        self.pozycja_y = y

    def set_zyje_false(self):
        self.zyje = False

    # --- Logic ---
    def wieksza_sila_od(self, other) -> bool:
        return self.sila >= other.get_sila()

    def get_random_dir(self) -> int:
        return random.randint(0, 3)

    def is_in_bounds(self, x: int, y: int) -> bool:
        max_x = self.swiat.grid_width
        max_y = self.swiat.grid_height
        return 0 <= x < max_x and 0 <= y < max_y

    def znajdz_wolne_pole_obok(self) -> Tuple[int, int]:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(dirs)  # randomize directions

        for dx, dy in dirs:
            new_x = self.pozycja_x + dx
            new_y = self.pozycja_y + dy
            if self.is_in_bounds(new_x, new_y) and self.swiat.find_organism_at(new_x, new_y) is None:
                return (new_x, new_y)

        return (-1, -1)  # No space found

    def czy_odbil_atak(self, atakujacy) -> bool:
        return False  # Override in subclasses like Zolw

    def wplyw_na_sile(self, atakujacy):
        pass  # Override if special behavior
