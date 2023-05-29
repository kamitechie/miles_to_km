from tkinter import *


def convert():
    miles = float(entry_box.get())
    km = round(miles*1.609344)
    label_2["text"] = f"{km}"


window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(width=150, height=90)
window.config(padx=20, pady=20)

label = Label(text="is equal to")
label.grid(column=0, row=1)

entry_box = Entry(width=10)

entry_box.grid(column=1, row=0)

label_2 = Label(text="0")
label_2.grid(column=1, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
