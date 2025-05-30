import random
import logging

from symulacja.classes.organizm import Organizm


class Zwierze(Organizm):
    def __init__(self, sila, inicjatywa, x, y, swiat):
        super().__init__(sila, inicjatywa, x, y, swiat)

    def akcja(self):
        if self.swiat is None:
            raise RuntimeError("Błąd: swiat == None")

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right
        dx, dy = directions[self.get_random_dir()]

        from_x = self.pozycja_x
        from_y = self.pozycja_y
        new_x = from_x + dx
        new_y = from_y + dy

        if not self.is_in_bounds(new_x, new_y):
            return

        other = self.swiat.find_organism_at(new_x, new_y)

        if other is None:
            self.set_pozycja(new_x, new_y)
            self.swiat.nowy_log(f"{self.nazwa()} przesunęło się na ({new_x}, {new_y})")
        else:
            self.kolizja(from_x, from_y, other)

    def kolizja(self, from_x, from_y, other):
        if type(self) == type(other):
            new_x, new_y = self.znajdz_wolne_pole_obok()
            if new_x == -1 and new_y == -1:
                return
            potomek = self.dodaj_potomka(new_x, new_y)
            if potomek:
                self.swiat.dodaj_organizm(potomek)
                self.swiat.log(f"{self.nazwa()} i {other.nazwa()} rozmnażają się na ({new_x}, {new_y})")
            else:
                self.swiat.log("Nie udało się stworzyć potomka – błąd.")
            return

        if other.czy_odbil_atak(self):
            self.set_pozycja(from_x, from_y)
            self.swiat.log(f"{self.nazwa()} nieudany atak – odbity przez {other.nazwa()} na ({self.pozycja_x}, {self.pozycja_y})")
            return

        other.wplyw_na_sile(self)

        if self.sila < 0:
            self.set_zyje_false()
            self.swiat.log(f"{self.nazwa()} został zatruty przez {other.nazwa()}")
            return

        if self.wieksza_sila_od(other):
            self.set_pozycja(other.get_pozycja_x(), other.get_pozycja_y())
            other.set_zyje_false()
            self.swiat.log(f"{self.nazwa()} zabił {other.nazwa()} na ({other.get_pozycja_x()}, {other.get_pozycja_y()})")
        else:
            self.set_zyje_false()
            self.swiat.log(f"{other.nazwa()} zabił {self.nazwa()} na ({self.get_pozycja_x()}, {self.get_pozycja_y()})")
