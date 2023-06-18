import tkinter as tk


def get_choice_text(checkbox_var_1, checkbox_var_2):
    if checkbox_var_1.get() == 1 and checkbox_var_2.get() == 1:
        result = "Music and Video"
    elif checkbox_var_1.get() == 1:
        result = "Music only"
    elif checkbox_var_2.get() == 1:
        result = "Video only"
    else:
        result = "Nothing"
    return result


def main():
    top = tk.Tk()

    checkbox_var_1 = tk.IntVar()
    checkbox_var_2 = tk.IntVar()

    checkbox_1 = tk.Checkbutton(top, text="Music", variable=checkbox_var_1)
    checkbox_1.pack()

    checkbox_2 = tk.Checkbutton(top, text="Video", variable=checkbox_var_2)
    checkbox_2.pack()

    button = tk.Button(top, text="Print Choice", command=lambda: print(get_choice_text(checkbox_var_1, checkbox_var_2)))
    button.pack()

    top.mainloop()
