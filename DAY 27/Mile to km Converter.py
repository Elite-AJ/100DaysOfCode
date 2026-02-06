#mile to km converter using Tkinter

from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width= 300, height= 300)
window.config(padx=10, pady=10)

mile_input = Entry(width=20)
mile_input.grid(column=1, row=0)
window.config(padx=50, pady=50)

first_label = Label(text="miles")
first_label.grid(column=2, row=0)
window.config(padx=50, pady=50)

second_label = Label(text="is equal to")
second_label.grid(column=0, row=1)
window.config(padx=50, pady=50)

third_label = Label(text="")
third_label.grid(column=1, row=1)
window.config(padx=50, pady=50)

fourth_label = Label(text="km")
fourth_label.grid(column=2, row=1)
window.config(padx=50, pady=50)

def button_clicked():
    miles = float(Entry.get(mile_input))
    km = round(miles * 1.60934, 2)
    third_label.config(text=km)

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)
window.config(padx= 50, pady=50)

window.mainloop()