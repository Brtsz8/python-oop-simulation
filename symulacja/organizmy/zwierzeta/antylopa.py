import random

from symulacja.organizmy.zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=4, inicjatywa=4, pozycja_x=x, pozycja_y=y, swiat=swiat)

    def rysowanie(self):
        return 'A'

    def nazwa(self):
        return "Antylopa"

    def dodaj_potomka(self, x, y):
        try:
            return Antylopa(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodej antylopy: {e}")
            return None

    def get_random_dir(self):
        return random.randint(0, 11)

    def czy_ucieka(self):
        return self.get_random_dir() % 2 == 0

    def akcja(self):
        dir = self.get_random_dir()
        move_x = [0, 0, -1, 1, -2, 2, 0, 0, 1, 1, -1, -1]
        move_y = [-1, 1, 0, 0, 0, 0, -2, 2, 1, -1, 1, -1]

        from_x = self.pozycja_x
        from_y = self.pozycja_y
        new_x = from_x + move_x[dir]
        new_y = from_y + move_y[dir]

        if not self.is_in_bounds(new_y, new_x):
            return

        other = self.swiat.find_organism_at(new_x, new_y)

        if other is None:
            self.set_pozycja(new_x, new_y)
            self.swiat.nowy_log(f"{self.nazwa()} przesuwa się na nową pozycję x:{new_x}, y:{new_y}")
        else:
            self.kolizja(from_x, from_y, other)

    def kolizja(self, from_x, from_y, other):
        if isinstance(other, Antylopa):
            super().kolizja(from_x, from_y, other)
            return

        if not self.czy_ucieka():
            self.swiat.nowy_log(f"{self.nazwa()} na x:{self.pozycja_x} y:{self.pozycja_y} nie ucieka")
            super().kolizja(from_x, from_y, other)
        else:
            kierunki = list(zip([0, 0, -1, 1], [-1, 1, 0, 0]))
            for dx, dy in kierunki:
                new_x = self.pozycja_x + dx
                new_y = self.pozycja_y + dy
                if self.is_in_bounds(new_y, new_x) and self.swiat.find_organism_at(new_x, new_y) is None:
                    self.set_pozycja(new_x, new_y)
                    self.swiat.nowy_log(f"{self.nazwa()} ucieka na pole x:{new_x} y:{new_y}")
                    return
            self.swiat.nowy_log(f"{self.nazwa()} próbowała uciekać, ale nie miała gdzie")

    def czy_odbil_atak(self, atakujacy):
        if not self.czy_ucieka():
            self.swiat.nowy_log(f"{self.nazwa()} na x:{self.pozycja_x} y:{self.pozycja_y} nie ucieka")
            return False

        kierunki = list(zip([0, 0, -1, 1], [-1, 1, 0, 0]))
        for dx, dy in kierunki:
            new_x = self.pozycja_x + dx
            new_y = self.pozycja_y + dy
            if self.is_in_bounds(new_y, new_x) and self.swiat.find_organism_at(new_x, new_y) is None:
                self.set_pozycja(new_x, new_y)
                self.swiat.nowy_log(f"{self.nazwa()} ucieka na pole x:{new_x} y:{new_y}")
                return True
        return False
