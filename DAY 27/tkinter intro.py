from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)

#Label
my_label = Label(text= "I am a Label")
my_label.grid(column=0, row=0)

def button_clicked():
    input_txt = input.get()
    my_label.config(text= input_txt)

my_Button = Button(text="Click  me", command=button_clicked)
my_Button.grid(column=1, row=1)

input = Entry(width=20)
input.grid(column=3, row=3)

my_new_button = Button(text="You like what you see?")
my_new_button.grid(column=2, row=0)

#mile to km converter using Tkinter







window.mainloop()