import tkinter as tk
import tkinter.messagebox as msg


def order_msg_box(top, lst):
    msg.showinfo("your Order", get_order_text(lst))
    top.destroy()  # closes the main window


def get_order_text(lst):
    result = "One pizza with"
    if lst.size() == 0:
        result += " nothing"
    else:
        for item in lst.get(0, tk.END):
            result += "\n* " + item
    return result


def main():
    default_options = (
        "Tomatoes", "Bellpeppers", "Eggplants", "Broccoli", "Corn", "Arugula", "Olives", "Onions", "Chilies",
        "Mushrooms", "Artichokes", "Mozzarella", "Gorgonzola")

    # numerical constants: describe width and height of the interface
    n = len(default_options)
    w = 6

    top = tk.Tk()
    top.title("Order your custom pizza!")

    buttons = []
    for i, ingredient in enumerate(default_options):
        buttons.append(tk.Button(top, text=ingredient, command=lambda c=i: lst.insert(tk.END, buttons[c]["text"])))

        buttons[i].grid(column=0, row=i, columnspan=w,  # use W cells in the grid
                        sticky="WE"  # fill the entire width of the grid
                        )

    txt = tk.Entry(top)
    txt.grid(column=0, row=n, columnspan=w - 1)

    tk.Button(top, text=">", command=lambda: lst.insert(tk.END, txt.get())).grid(column=w - 1, row=n)

    lst = tk.Listbox(top, height=2 * n)
    lst.grid(column=w + 1, row=0, rowspan=n)

    tk.Button(top, text="remove",
              command=lambda: lst.delete(*lst.curselection()) if len(lst.curselection()) else None).grid(column=w + 1,
                                                                                                         row=n,
                                                                                                         sticky="WE")

    tk.Button(  #
        top,  #
        text="Order!",  #
        command=lambda: order_msg_box(top, lst)  #
    ).grid(  #
        column=0, row=n + 1,  #
        columnspan=w + 2,  #
        sticky="WE"  #
    )

    top.mainloop()
