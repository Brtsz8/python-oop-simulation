from symulacja.classes.organizmy.roslina import Roslina
from symulacja.classes.organizmy.zwierze import Zwierze
from symulacja.classes.organizmy.zwierzeta.cyberowca import Cyberowca


class Barszcz(Roslina):
    def __init__(self, x, y, swiat):
        super().__init__(sila=99, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return '!'

    def nazwa(self):
        return "Barszcz_Sosnowskiego"

    def dodaj_potomka(self, x, y):
        return Barszcz(x, y, self.get_swiat())

    def kolizja(self, from_x, from_y, other):
        if isinstance(other,Cyberowca):
            return
        log = f"{self.nazwa()} został zjedzony - {other.nazwa()} ginie"
        other.set_sila(-1)
        self.get_swiat().dodaj_log(log)
        self.zyje = False

    def wplyw_na_sile(self, atakujacy):
        if isinstance(atakujacy,Cyberowca):
            return
        log = f"{self.nazwa()} został zjedzony - {atakujacy.nazwa()} ginie"
        self.swiat.nowy_log(log)
        atakujacy.set_sila(-1)

    def akcja(self):
        log_entries = []
        x, y = self.pozycja_x, self.pozycja_y

        deltas = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        for new_x, new_y in deltas:
            if self.is_in_bounds(new_x, new_y):
                sasiad = self.swiat.find_organism_at(new_x, new_y)
                if isinstance(sasiad, Zwierze) and not isinstance(sasiad,Cyberowca):
                    log_entries.append(f"{self.nazwa()} zabija {sasiad.nazwa()} który był za blisko")
                    sasiad.zyje = False

        for log in log_entries:
            self.swiat.nowy_log(log)

        super().akcja()
