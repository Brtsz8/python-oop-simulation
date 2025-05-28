from symulacja.classes.organizmy.roslina import Roslina
from symulacja.classes.organizmy.zwierze import Zwierze

class Barszcz(Roslina):
    def __init__(self, x, y, swiat):
        super().__init__(sila=99, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return '!'

    def nazwa(self):
        return "Barszcz Sosnowskiego"

    def dodaj_potomka(self, x, y):
        return Barszcz(x, y, self.get_swiat())

    def kolizja(self, from_x, from_y, other):
        log = f"{self.nazwa()} został zjedzony - {other.nazwa()} ginie"
        other.set_sila(-1)
        self.get_swiat().dodaj_log(log)
        self.set_zyje(False)

    def wplyw_na_sile(self, atakujacy):
        log = f"{self.nazwa()} został zjedzony - {atakujacy.nazwa()} ginie"
        self.get_swiat().dodaj_log(log)
        atakujacy.set_sila(-1)

    def akcja(self):
        log_entries = []
        x, y = self.x, self.y
        win = self.get_swiat().get_win()

        deltas = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        for new_x, new_y in deltas:
            if self.is_in_bounds(win, new_y, new_x):
                sasiad = self.get_swiat().find_organism_at(new_x, new_y)
                if isinstance(sasiad, Zwierze):
                    log_entries.append(f"{self.nazwa()} zabija {sasiad.nazwa()} który był za blisko")
                    sasiad.set_zyje(False)

        for log in log_entries:
            self.get_swiat().dodaj_log(log)

        super().akcja()
