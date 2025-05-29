from symulacja.views.lvl_selection_view import LvlSelectionView
from utils.settings import Settings
from views.world_selection_view import WorldSelectionView
#from views.lvl_selection_view import LvlSelectionView
#from views.sim_view import SimView

class AppController:
    def __init__(self,root):
        self.root = root
        self.settings = Settings("files/conf.txt")
        self.world_selection()

    def world_selection(self):
        self.clear_window()
        WorldSelectionView(self.root,self)

    def show_lvl_selection(self):
        self.clear_window()
        LvlSelectionView(self.root,self)

    #funkcja usuwa wszystkie widgety z roota, jednoczesnie go czyszczac
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()