from symulacja.classes.organizmy.roslina import Roslina


class Trawa(Roslina):
    def __init__(self, x, y, swiat):
        super().__init__(sila=0, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return (50, 150, 50)

    def nazwa(self):
        return "Trawa"

    def dodaj_potomka(self, x, y):
        try:
            return Trawa(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodego wilka: {e}")
            return None