from symulacja.organizmy.zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=9, inicjatywa=5, pozycja_x=x, pozycja_y=y, swiat=swiat)

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
