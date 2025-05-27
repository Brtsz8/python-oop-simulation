import tkinter as tk

# Main Tkinter app
def main():
    root = tk.Tk()
    root.title("Hive Grid")

    canvas_width = 800
    canvas_height = 600

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    draw_hive_grid(canvas, rows=10, cols=10, size=30)

    root.mainloop()

if __name__ == "__main__":
    main()
