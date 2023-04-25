import tkinter


window = tkinter.Tk()
window.title('Pizza Selection Menu')

pizza_mode = tkinter.StringVar()
pizza_mode.set("Onion Topping")

toppings = [
    ("Pepperoni", "Pepperoni Topping"),
    ("Cheese", "Cheese Topping"),
    ("Mushroom", "Mushroom Topping"),
    ("Onion", "Onion Topping")
]


def clicked():
    global selected_pizza_label

    selected_pizza_label.destroy()
    selected_pizza_label = tkinter.Label(window, text="You selected Pizza with: " + pizza_mode.get())
    selected_pizza_label.pack(anchor='w')


for topping, pizza_name in toppings:
    tkinter.Radiobutton(window, text=topping, variable=pizza_mode, value=pizza_name,
                        command=clicked).pack(anchor='w')

selected_pizza_label = tkinter.Label(window, text="You selected Pizza with: " + pizza_mode.get())
selected_pizza_label.pack(anchor='w')


window.mainloop()

# r = tkinter.IntVar()
# r.set(2)
#
#
# def clicked(num):
#     tkinter.Label(window, text=num).pack()
#
#
# tkinter.Radiobutton(window, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# tkinter.Radiobutton(window, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()
#
# my_label = tkinter.Label(window, text=r.get())
# my_label.pack()
