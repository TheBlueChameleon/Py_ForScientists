import tkinter as tk
import tkinter.messagebox


def main():
    top = tk.Tk()
    top.geometry("200x100+10+20")

    def callback_hello_world():
        tk.messagebox.showinfo(  #
            "Hello Python",  # window title
            "Hello World"  # window text
        )

    button = tk.Button(top,  #
                       text="Hello",  #
                       command=callback_hello_world)
    button.fg = "#FF0000"
    button.place(x=50, y=50)

    top.mainloop()
