import random

from symulacja.classes.organizm import Organizm


class Roslina(Organizm):
    def __init__(self, sila, x, y, swiat):
        super().__init__(sila, inicjatywa=0, pozycja_x=x, pozycja_y=y, swiat=swiat)

    def czy_rosnie(self):
        return random.randint(0, 9)

    def akcja(self):
        if self.swiat is None:
            raise RuntimeError("Błąd: swiat == None")

        # ~30% szans na rozrost (roslina nie rośnie co turę)
        if self.czy_rosnie() % 3 != 0:
            return

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # góra, dół, lewo, prawo
        dx, dy = directions[self.get_random_dir()]

        from_x = self.pozycja_x
        from_y = self.pozycja_y
        new_x = from_x + dx
        new_y = from_y + dy

        if not self.is_in_bounds(new_x, new_y):
            return

        other = self.swiat.find_organism_at(new_x, new_y)
        if other is None:
            potomek = self.dodaj_potomka(new_x, new_y)
            if potomek:
                self.swiat.dodaj_organizm(potomek)
                self.swiat.log(f"{self.nazwa()} rozprzestrzenia się na ({new_x}, {new_y})")
            else:
                print("Nie udało się stworzyć potomka – błąd programu.")
        else:
            # Rośliny nie wykonują kolizji (chyba że np. barszcz Sosnowskiego)
            pass

    def kolizja(self, from_x, from_y, other):
        pass  # może zostać nadpisane w roślinach specjalnych
