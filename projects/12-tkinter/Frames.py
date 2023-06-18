import tkinter as tk


def main():
    root = tk.Tk()

    frame_top = tk.Frame(root)
    frame_top.pack()

    frame_bottom = tk.Frame(root)
    frame_bottom.pack(side=tk.BOTTOM, fill=tk.X)

    button_red = tk.Button(frame_top, text="Red", fg="red")
    button_red.pack(side=tk.LEFT)

    button_green = tk.Button(frame_top, text="Green", fg="green")
    button_green.pack(side=tk.LEFT)

    button_blue = tk.Button(frame_top, text="Blue", fg="blue")
    button_blue.pack(side=tk.LEFT)

    button_black = tk.Button(frame_bottom, text="Black", fg="black")
    button_black.pack(side=tk.BOTTOM, fill=tk.X)

    root.mainloop()
