import tkinter as tk

def main():
    top = tk.Tk()

    frame_top = tk.Frame(top)
    frame_top.pack(side=tk.TOP)

    frame_btm = tk.Frame(top)
    frame_btm.pack(side=tk.BOTTOM, fill=tk.X)

    label = tk.Label(frame_top, #
                  text = "User Name"
    )
    label.pack(side = tk.LEFT)

    entry = tk.Entry(frame_top)
    entry.pack(side = tk.RIGHT)

    button = tk.Button(
        frame_btm,
        text="show",
        command = lambda : print(entry.get())
    )
    button.pack(fill=tk.X)

    top.mainloop()