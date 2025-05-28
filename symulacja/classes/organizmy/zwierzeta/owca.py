from symulacja.classes.organizmy.zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=4, inicjatywa=4, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return (200, 200, 200)  # Kolor szary dla owcy w pygame (RGB)

    def nazwa(self):
        return "Owca"

    def dodaj_potomka(self, x, y):
        try:
            return Owca(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodej owcy: {e}")
            return None
