import tkinter as tk


def main():
    root = tk.Tk()

    num = 1
    for row in range(6):
        for column in range(6):
            tk.Button(root,  #
                      text=str(num),  #
                      borderwidth=1,  #
                      command=lambda button_id=num: print(f"ok, {button_id}")  #
                      ).grid(row=row, column=column)
            num += 1

    root.mainloop()
