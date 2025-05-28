from symulacja.classes.organizmy.roslina import Roslina
import random

class Jagody(Roslina):
    def __init__(self, x, y, swiat):
        super().__init__(sila=10, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return '%'

    def nazwa(self):
        return "Wilcze Jagody"

    def dodaj_potomka(self, x, y):
        return Jagody(x, y, self.get_swiat())

    def kolizja(self, from_x, from_y, other):
        log = f"{self.nazwa()} zjedzone - ginie {other.nazwa()} na polu x:{other.x} y:{other.y}"
        other.set_sila(-1)  # zabija atakującego
        self.get_swiat().dodaj_log(log)
        self.set_zyje(False)

    def wplyw_na_sile(self, atakujacy):
        log = f"{self.nazwa()} zjedzone - ginie {atakujacy.nazwa()} na polu x:{atakujacy.x} y:{atakujacy.y}"
        self.get_swiat().dodaj_log(log)
        atakujacy.set_sila(-1)
