from symulacja.classes.organizmy.zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=2, inicjatywa=1, x=x, y=y, swiat=swiat)

    def akcja(self):
        if self.get_random_dir() == 0:  # 25% szansy na ruch (1 z 4 kierunków)
            super().akcja()

    def rysowanie(self):
        return 'Z'  # lub (0, 100, 0) dla ciemnozielonego w Pygame

    def nazwa(self):
        return "Zolw"

    def dodaj_potomka(self, x, y):
        try:
            return Zolw(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodego żółwia: {e}")
            return None

    def czy_odbil_atak(self, atakujacy):
        return atakujacy.get_sila() < 5
