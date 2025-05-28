from symulacja.classes.organizmy.roslina import  Roslina

class Guarana(Roslina):
    def __init__(self, x, y, swiat):
        super().__init__(sila=0, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return '&'

    def nazwa(self):
        return "Guarana"

    def dodaj_potomka(self, x, y):
        return Guarana(x, y, self.get_swiat())

    def kolizja(self, from_x, from_y, other):
        log = (
            f"{other.nazwa()} na polu x:{self.x} y:{self.y} "
            f"zyskuje siłę dzięki {self.nazwa()}"
        )
        other.set_sila(other.get_sila() + 3)
        self.get_swiat().dodaj_log(log)
        self.set_zyje(False)

    def wplyw_na_sile(self, atakujacy):
        log = (
            f"{atakujacy.nazwa()} na polu x:{self.x} y:{self.y} "
            f"zyskuje siłę dzięki {self.nazwa()}"
        )
        self.get_swiat().dodaj_log(log)
        atakujacy.set_sila(atakujacy.get_sila() + 3)
