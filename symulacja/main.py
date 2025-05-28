import tkinter as tk
from utils.settings import Settings
# Main Tkinter app
def main():
    root = tk.Tk()
    root.title("Bartosz Pacyga s203833")
    settings = Settings("files/conf.txt")
    
    #dodac mozliwosc sterowaniem tym z configu
    canvas_width = 800
    canvas_height = 600
    #dodanie mozliwosci wybrania swiata


    #zaladowanie konkretnego swiata


    #wybor zwierzat i pozycji

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
