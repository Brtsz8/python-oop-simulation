from symulacja.classes.organizmy.roslina import Roslina
import random

class Mlecz(Roslina):
    def __init__(self, x, y ,swiat):
        super().__init__(sila=0,x=x,y=y, swiat=swiat)

    def rysowanie(self):
        return '@'

    def nazwa(self):
        return "Mlecz"

    def dodaj_potomka(self,x,y):
        return Mlecz(x,y,self.get_swiat())

    def akcja(self):
        logi = []
        proby = 3
        while proby:
            proby -=1
            if self.czy_rosnie() % 3 != 0:
                continue

            kierunki = [(0,-1),(0,1),(-1,0),(1,0)]
            dx,dy = random.choice(kierunki)
            new_x = self.pozycja_x + dx
            new_y = self.pozycja_y + dy

            if not self.is_in_bounds(new_x,new_y):
                continue

            if self.swiat.find_organism_at(new_x,new_y) is None:
                potomek = self.dodaj_potomka(new_x,new_y)
                if potomek is not None:
                    self.get_swiat().nowy_organizm(potomek)
                    logi.append(f"Dodano nowy {potomek.nazwa()} na x:{new_x} y:{new_y}")
            for wpis in logi:
                self.swiat.nowy_log(wpis)
