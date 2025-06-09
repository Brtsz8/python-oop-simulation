from abc import ABC, abstractmethod
#zwierzeta
from symulacja.classes.organizmy.zwierzeta.wilk import Wilk
from symulacja.classes.organizmy.zwierzeta.owca import Owca
from symulacja.classes.organizmy.zwierzeta.lis import Lis
from symulacja.classes.organizmy.zwierzeta.zolw import Zolw
from symulacja.classes.organizmy.zwierzeta.antylopa import Antylopa
from symulacja.classes.organizmy.zwierzeta.czlowiek import Czlowiek
from symulacja.classes.organizmy.zwierzeta.cyberowca import Cyberowca
#rosliny
from symulacja.classes.organizmy.rosliny.trawa import Trawa
from symulacja.classes.organizmy.rosliny.mlecz import Mlecz
from symulacja.classes.organizmy.rosliny.guarana import Guarana
from symulacja.classes.organizmy.rosliny.jagody import Jagody
from symulacja.classes.organizmy.rosliny.barszcz import Barszcz

class Swiat(ABC):
    def __init__(self, win, log_window, settings):
        self.win = win
        self.log_window = log_window
        self.organizmy = []
        self.nowe = []
        self.logs = []
        self.top_log = 0
        self.command = None
        self.grid_width = settings.cell_size * settings.width
        self.grid_height = settings.cell_size * settings.height
        self.cell_size = settings.cell_size

    def get_win(self):
        return self.win

    def get_log(self):
        return self.log_window

    def get_top_log_index(self):
        return self.top_log

    def get_command(self):
        return self.command

    def set_top_log_index(self, index):
        if 0 <= index <= len(self.logs):
            self.top_log = index
            self.wyswietl_logi(index)

    def set_command(self, command):
        self.command = command
        self.wykonaj_ture()
        print(f"Input {self.command}")


    def nowy_organizm(self, organizm):
        self.nowe.append(organizm)

    def nowy_log(self, log):
        self.logs.append(log)

    #funkcja wyswietla wszystki logi w side_panel
    def wyswietl_logi(self, pierwszy_log = 0):
        if not self.log_window:
            return

        self.log_window.config(state='normal')  # umożliw edycję
        self.log_window.delete("1.0", "end")  # wyczyść całość

        max_lines = int(self.log_window['height']) - 1
        for i in range(pierwszy_log, min(pierwszy_log + max_lines, len(self.logs))):
            self.log_window.insert('end', self.logs[i] + '\n')

        self.log_window.see("end")  # scroll do końca
        self.log_window.config(state='disabled')  # zablokuj edycję

    def wykonaj_ture(self):
        self.sortuj_wszystkie()
        for organizm in self.organizmy:
            if organizm.get_zyje():
                organizm.akcja()
        self.usun_zabite()
        self.organizmy.extend(self.nowe)
        self.nowe.clear()
        self.rysuj_swiat()
        self.wyswietl_logi(self.top_log)
        #logs for testing
        #print(self.organizmy)

    def sortuj_wszystkie(self):
        self.organizmy.sort(key=lambda o: o.get_inicjatywa(), reverse=True)

    def usun_zabite(self):
        self.organizmy = [o for o in self.organizmy if o.get_zyje()]

    def save(self, file_path):
        with open(file_path, 'w') as file:
            file.write("Win\n")
            for organizm in self.organizmy:
                line = f"{organizm.nazwa()} {organizm.get_pozycja_x()} {organizm.get_pozycja_y()} {organizm.get_sila()}"
                if organizm.nazwa() == "Czlowiek":
                    line += f" {int(organizm.get_umiejetnosc_aktywna())} {organizm.get_dlugosc_umiejetnosci()} {organizm.get_dlugosc_regeneracji()}"
                file.write(line + "\n")
            file.write("LogWindow\n")
            for log in self.logs:
                file.write(log + "\n")

    def load(self, file_path):
        self.organizmy.clear()
        self.logs.clear()

        with open(file_path, 'r') as file:
            lines = file.readlines()

        i = 1
        while i < len(lines) and lines[i].strip() != "LogWindow":
            parts = lines[i].split()
            nazwa = parts[0]
            x, y, sila = int(parts[1]), int(parts[2]), int(parts[3])

            organizm = self._stworz_organizm_po_nazwie(nazwa, x, y)
            if organizm:
                organizm.set_sila(sila)

                # Specjalna obsługa Człowieka
                if nazwa == "Czlowiek" and len(parts) >= 7:
                    umiejetnosc = bool(int(parts[4]))
                    dlugosc_umiejetnosci = int(parts[5])
                    dlugosc_regeneracji = int(parts[6])

                    organizm.set_umiejetnosc_aktywna(umiejetnosc)
                    organizm.set_dlugosc_umiejetnosci(dlugosc_umiejetnosci)
                    organizm.set_dlugosc_regeneracji(dlugosc_regeneracji)

                self.nowy_organizm(organizm)
            i += 1

        for log in lines[i + 1:]:
            if log.strip():
                self.logs.append(log.strip())

    def _stworz_organizm_po_nazwie(self, nazwa, x, y):
        mapping = {
            "Wilk": Wilk,
            "Owca": Owca,
            "Lis": Lis,
            "Zolw": Zolw,
            "Antylopa": Antylopa,
            "Czlowiek": Czlowiek,
            "Trawa": Trawa,
            "Mlecz": Mlecz,
            "Guarana": Guarana,
            "Wilcze_Jagody": Jagody,
            "Barszcz_Sosnowskiego": Barszcz,
            "Cyberowca" : Cyberowca
        }
        return mapping[nazwa](x, y, self) if nazwa in mapping else None

    def find_organism_at(self, x, y):
        for organizm in self.organizmy + self.nowe:
            if organizm.get_pozycja_x() == x and organizm.get_pozycja_y() == y:
                return organizm
        return None

    @abstractmethod
    def rysuj_swiat(self):
        pass

    def get_dirs(self, x = None):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def get_deltas(self, x: int, y: int) -> list[tuple[int, int]]:
        return [
            (x, y - 1),  # góra
            (x, y + 1),  # dół
            (x - 1, y),  # lewo
            (x + 1, y),  # prawo
        ]