import tkinter as tk
from tkinter import Frame, Button

import utils
from utils.settings import Settings
# Main Tkinter app
def main():
    window = tk.Tk()
    window.title("Bartosz Pacyga s203833")
    settings = Settings("files/conf.txt")

    #dodac mozliwosc sterowaniem tym z configu

    canvas_width = 800
    canvas_height = 600
    #dodanie mozliwosci wybrania swiata
    btn_swiat = Button(window,text = "Świat Kwadratowy", command=settings.set_map_sqr)
    btn_swiat_hex = Button(window,text = "Świat Hex", command=settings.set_map_hex)
    btn_swiat.pack()
    btn_swiat_hex.pack()
    #zaladowanie konkretnego swiata


    #wybor zwierzat i pozycji
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
