from symulacja.classes.organizmy.zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=3, inicjatywa=7, x=x, y=y, swiat=swiat)

    def rysowanie(self):
        return 'L'  # lub kolor np. (255, 165, 0) dla pomarańczowego w Pygame

    def nazwa(self):
        return "Lis"

    def dodaj_potomka(self, x, y):
        try:
            return Lis(x, y, self.swiat)
        except Exception as e:
            print(f"[BŁĄD] Nie udało się stworzyć młodego lisa: {e}")
            return None

    def akcja(self):
        if self.swiat is None:
            print("[BŁĄD] Brak dostępu do świata.")
            return

        dir = self.get_random_dir()
        move_x = [0, 0, -1, 1]
        move_y = [-1, 1, 0, 0]

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
        elif self.wieksza_sila_od(other):
            self.kolizja(from_x, from_y, other)
        else:
            self.swiat.nowy_log(f"{self.nazwa()} nie rusza się na pole x:{new_x} y:{new_y} - jest słabszy!")

