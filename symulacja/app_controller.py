from tkinter import Frame, Label

from utils.settings import Settings
from symulacja.views.world_selection_view import WorldSelectionView
from symulacja.views.lvl_selection_view import LvlSelectionView
from symulacja.views.sim_view import SimView

class AppController:
    def __init__(self,root):
        self.root = root
        self.settings = Settings("files/conf.txt")
        self.root.geometry(f"{self.settings.width * self.settings.cell_size + 300}" + "x" +
                           f"{self.settings.height * self.settings.cell_size}")
        self.world_selection()

    def world_selection(self):
        self.clear_window()
        WorldSelectionView(self.root,self)

    def show_lvl_selection(self):
        self.clear_window()
        LvlSelectionView(self.root,self)

    def start_game(self):
        self.clear_window()
        canvas_frame = Frame(self.root)
        side_panel = Frame(self.root)

        canvas_frame.pack(side='left', fill='both', expand=True)
        side_panel.pack(side='right', fill='y')

        label = Label(side_panel, text="LOGI", bg="lightgrey")
        label.pack(side="top", fill="x")

        sim_view = SimView(self.root, controller=self,
                           lvl_path=self.settings.current_lvl,
                           canvas_frame=canvas_frame,
                           side_panel=side_panel)



    #funkcja usuwa wszystkie widgety z roota, jednoczesnie go czyszczac
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()