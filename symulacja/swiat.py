import pygame
import os

class Swiat:
    def __init__(self, screen, log_font):
        self.screen = screen
        self.log_font = log_font
        self.organizmy = []
        self.nowe = []
        self.logs = []
        self.top_log = 0
        self.command = 0
        self.cell_size = 20  # pixels
        self.grid_width = screen.get_width() // self.cell_size
        self.grid_height = screen.get_height() // self.cell_size - 5  # space for logs

    def nowy_organizm(self, organizm):
        self.nowe.append(organizm)

    def nowy_log(self, log):
        self.logs.append(log)

    def set_top_log_index(self, index):
        max_logs_display = 5
        if 0 <= index <= len(self.logs) - max_logs_display:
            self.top_log = index

    def wykonaj_ture(self):
        self.sortuj_wszystkie()
        for organizm in self.organizmy:
            if organizm.get_zyje():
                organizm.akcja()
        self.usun_zabite()
        self.organizmy.extend(self.nowe)
        self.nowe.clear()
        self.rysuj_swiat()

    def sortuj_wszystkie(self):
        self.organizmy.sort(key=lambda o: o.get_inicjatywa(), reverse=True)

    def usun_zabite(self):
        self.organizmy = [o for o in self.organizmy if o.get_zyje()]

    def rysuj_swiat(self):
        self.screen.fill((0, 0, 0))  # clear screen

        # Draw organisms
        for organizm in self.organizmy:
            x = organizm.get_pozycja_x() * self.cell_size
            y = organizm.get_pozycja_y() * self.cell_size
            pygame.draw.rect(self.screen, organizm.rysowanie(), (x, y, self.cell_size, self.cell_size))

        # Draw logs
        self.draw_logs()

        pygame.display.flip()

    def draw_logs(self):
        log_start_y = self.grid_height * self.cell_size + 5
        max_lines = 5
        for i in range(max_lines):
            log_index = self.top_log + i
            if log_index < len(self.logs):
                log_text = self.logs[log_index]
                rendered_text = self.log_font.render(log_text, True, (255, 255, 255))
                self.screen.blit(rendered_text, (5, log_start_y + i * 20))

    def find_organism_at(self, x, y):
        for o in self.organizmy + self.nowe:
            if o.get_pozycja_x() == x and o.get_pozycja_y() == y:
                return o
        return None

    def save(self, file_path):
        with open(file_path, 'w') as f:
            f.write("Win\n")
            for o in self.organizmy:
                f.write(f"{o.nazwa()} {o.get_pozycja_x()} {o.get_pozycja_y()} {o.get_sila()}\n")
            f.write("LogWindow\n")
            for log in self.logs:
                f.write(f"{log}\n")

    def load(self, file_path):
        self.organizmy.clear()
        self.logs.clear()

        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as f:
            lines = f.readlines()

        mode = None
        for line in lines:
            line = line.strip()
            if line == "Win":
                mode = "Win"
                continue
            elif line == "LogWindow":
                mode = "LogWindow"
                continue

            if mode == "Win":
                tokens = line.split()
                if len(tokens) != 4:
                    continue
                name, x, y, sila = tokens
                organizm = self.create_organizm(name, int(x), int(y))
                if organizm:
                    organizm.set_sila(int(sila))
                    self.nowy_organizm(organizm)
            elif mode == "LogWindow":
                self.logs.append(line)

    def create_organizm(self, name, x, y):
        # Replace with actual class mapping
        mapping = {
            "Wilk": Wilk,
            "Owca": Owca,
            "Lis": Lis,
            "Zolw": Zolw,
            "Antylopa": Antylopa,
            "Trawa": Trawa,
            "Mlecz": Mlecz,
            "Guarana": Guarana,
            "Wilcze Jagody": Jagody,
            "Barszcz Sosnowskiego": Barszcz,
            "Czlowiek": Czlowiek,
        }
        cls = mapping.get(name)
        return cls(x, y, self) if cls else None
