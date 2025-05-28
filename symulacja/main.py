import tkinter as tk
from tkinter import Frame, Button

import utils
from utils.settings import Settings
from app_controller import AppContreoller

# Main Tkinter app
def main():
    window = tk.Tk()
    window.title("Bartosz Pacyga s203833")
    settings = Settings("files/conf.txt")
    controller = AppContreoller(window)
    #dodac mozliwosc sterowaniem tym z configu

    # Create a label and bind it to the settings instance
    #label = tk.Label(window, text="No map type selected")
    #label.pack()

    # Let settings access the label so it can update it
    #settings.bind_label(label)

    # Buttons
    #btn_swiat = tk.Button(window, text="Świat Kwadratowy", command=settings.set_map_sqr)
    #btn_swiat_hex = tk.Button(window, text="Świat Hex", command=settings.set_map_hex)

    #btn_swiat.pack()
    #btn_swiat_hex.pack()

    window.mainloop()

    window.mainloop()

if __name__ == "__main__":
    main()
