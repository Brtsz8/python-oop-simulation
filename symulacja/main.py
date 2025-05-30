import tkinter as tk
from tkinter import Frame, Button

import utils
from utils.settings import Settings
from app_controller import AppController

# Main Tkinter app
def main():
    window = tk.Tk()
    window.title("Bartosz Pacyga s203833")
    controller = AppController(window)
    window.mainloop()

if __name__ == "__main__":
    main()
