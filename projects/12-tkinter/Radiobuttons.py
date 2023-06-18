import tkinter as tk


def get_choice_text(option_left, option_right):
    return chr(option_left.get() + 65) + str(option_right.get())


def main():
    top = tk.Tk()
    rows = 8

    option_left = tk.IntVar()
    option_right = tk.IntVar()

    for i in range(1, rows + 1):
        tk.Radiobutton(top,  #
                       text=chr(i + 64),  #
                       variable=option_left,  #
                       val=i  #
                       ).grid(row=i - 1, column=0)

    for i in range(1, rows + 1):
        tk.Radiobutton(top,  #
                       text=str(i),  #
                       variable=option_right,  #
                       val=i  #
                       ).grid(row=i - 1, column=1)

    tk.Button(top,  #
              text="Print Choice",  #
              command=lambda: print(get_choice_text(option_left, option_right))  #
              ).grid(row=rows, column=0, columnspan=2)

    # setting these values already selects the associated radio buttons
    option_left.set(3)
    option_right.set(3)

    top.mainloop()
