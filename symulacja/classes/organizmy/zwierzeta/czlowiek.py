from symulacja.classes.organizmy.zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=5, inicjatywa=4, x=x, y=y, swiat=swiat)
        self.umiejetnosc_aktywna = False
        self.dlugosc_umiejetnosci = 0
        self.dlugosc_regeneracji = 0

    def get_umiejetnosc_aktywna(self):
        return self.umiejetnosc_aktywna

    def get_dlugosc_umiejetnosci(self):
        return self.dlugosc_umiejetnosci

    def get_dlugosc_regeneracji(self):
        return self.dlugosc_regeneracji

    def set_umiejetnosc_aktywna(self, aktywnosc):
        self.umiejetnosc_aktywna = aktywnosc

    def set_dlugosc_umiejetnosci(self, dlugosc):
        self.dlugosc_umiejetnosci = dlugosc

    def set_dlugosc_regeneracji(self, dlugosc):
        self.dlugosc_regeneracji = dlugosc

    def rysowanie(self):
        return "C"

    def nazwa(self):
        return "Czlowiek"

    def akcja(self):
        logi = self.swiat.logs
        direction = self.swiat.get_command()

        # obsługa umiejętności
        if self.dlugosc_umiejetnosci > 0:
            self.dlugosc_umiejetnosci -= 1
        if self.dlugosc_regeneracji > 0:
            self.umiejetnosc_aktywna = False
            self.dlugosc_regeneracji -= 1
            logi.append("Umiejętność regeneruje się!")
        if self.dlugosc_umiejetnosci == 0 and self.umiejetnosc_aktywna:
            self.umiejetnosc_aktywna = False
            self.dlugosc_regeneracji = 5
            logi.append("Umiejętność przestała działać!")

        dx, dy = 0, 0
        if direction == "Up":
            dy = -1
        elif direction == "Down":
            dy = 1
        elif direction == "Left":
            dx = -1
        elif direction == "Right":
            dx = 1
        elif direction == "Skill":
            if self.umiejetnosc_aktywna:
                logi.append("Umiejętność już aktywna!")
            elif self.dlugosc_regeneracji > 0:
                logi.append(f"Umiejętność dostępna za {self.dlugosc_regeneracji} tur!")
            else:
                self.umiejetnosc_aktywna = True
                self.dlugosc_umiejetnosci = 5
                logi.append("Tarcza Azura aktywowana!")
            return

        new_x = self.pozycja_x + dx
        new_y = self.pozycja_y + dy
        if self.is_in_bounds(new_x, new_y):
            other = self.swiat.find_organism_at(new_x, new_y)
            if other:
                self.kolizja(self.pozycja_x, self.pozycja_y, other)
            else:
                self.pozycja_x = new_x
                self.pozycja_y = new_y
                logi.append(f"Człowiek przesuwa się na ({new_x}, {new_y})")
