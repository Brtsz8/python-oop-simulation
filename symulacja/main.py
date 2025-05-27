import tkinter as tk
import math

# Hexagon drawing function
def draw_hexagon(canvas, x, y, size, color="black"):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        points.extend([px, py])
    canvas.create_polygon(points, outline=color, fill='', width=1)

# Hive grid function
def draw_hive_grid(canvas, rows, cols, size):
    width = size * 2
    height = math.sqrt(3) * size
    for row in range(rows):
        for col in range(cols):
            x_offset = col * 1.5 * size
            y_offset = row * height + (height / 2 if col % 2 else 0)
            draw_hexagon(canvas, x_offset + size, y_offset + size, size)

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
