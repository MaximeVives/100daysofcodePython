from tkinter import *


def convert_distance():
    miles_value = float(miles_entry.get())
    convert = miles_value * 1.609

    result_lab["text"] = str(convert)


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=250, height=80)


miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_lab = Label(text="Miles").grid(column=2, row=0)

text_equal = Label(text="is equal to").grid(column=0, row=1)

result_lab = Label(text="0")
result_lab.grid(column=1, row=1)

unit_lab = Label(text="Km").grid(column=2, row=1)


calculate_btn = Button(text="Calculate", command=convert_distance).grid(column=1, row=2)

window.mainloop()
