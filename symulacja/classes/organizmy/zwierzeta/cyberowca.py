from symulacja.classes.organizmy.zwierze import Zwierze


class Cyberowca(Zwierze):
    def __init__(self, x, y, swiat):
        super().__init__(sila=11, inicjatywa=4, x=x, y=y, swiat=swiat)

    def nazwa(self):
        return "Cyberowca"

    def rysowanie(self):
        return "Y"  # symbol na planszy

    def znajdz_barszcz(self):
        barszcze = [
            org for org in self.swiat.organizmy if org.nazwa() == "Barszcz_Sosnowskiego"
        ]
        if not barszcze:
            return None

        # znajdź najbliższy
        najblizszy = min(
            barszcze, key=lambda b: abs(b.pozycja_x - self.pozycja_x) + abs(b.pozycja_y - self.pozycja_y)
        )
        return najblizszy

    def akcja(self):
        cel = self.znajdz_barszcz()
        dx, dy = 0, 0

        if cel:
            if cel.pozycja_x > self.pozycja_x:
                dx = 1
            elif cel.pozycja_x < self.pozycja_x:
                dx = -1
            elif cel.pozycja_y > self.pozycja_y:
                dy = 1
            elif cel.pozycja_y < self.pozycja_y:
                dy = -1

        nowy_x = self.pozycja_x + dx
        nowy_y = self.pozycja_y + dy

        if not self.is_in_bounds(nowy_x, nowy_y):
            return

        inny = self.swiat.find_organism_at(nowy_x, nowy_y)
        if inny:
            if inny.nazwa() == "Barszcz_Sosnowskiego":
                inny.zyje = False
                self.swiat.logs.append("Cyberowca niszczy Barszcz Sosnowskiego!")
            else:
                self.kolizja(self.pozycja_x, self.pozycja_y, inny)
        else:
            self.pozycja_x = nowy_x
            self.pozycja_y = nowy_y
            self.swiat.logs.append(f"Cyberowca przesuwa się na ({nowy_x},{nowy_y})")
