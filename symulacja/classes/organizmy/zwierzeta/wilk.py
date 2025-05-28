from symulacja.classes.organizmy.zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=9, inicjatywa=5, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return (50, 50, 50)  # Kolor ciemnoszary w RGB, lub inny charakterystyczny

    def nazwa(self):
        return "Wilk"

    def dodaj_potomka(self, x, y):
        try:
            return Wilk(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodego wilka: {e}")
            return None
