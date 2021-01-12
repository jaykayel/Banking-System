from datetime import date
from tkinter import *
import terminal

# ask for input
master = Tk()
Label(master, text="Enter Card Number").grid(row=0)
Label(master, text="Enter PIN").grid(row=1)

card_number = Entry(master)
pin = Entry(master)

card_number.grid(row=0, column=1)
pin.grid(row=1, column=1)

Button(master, text='Exit', command=master.quit).grid(row=3, column=0, stixky=W, pady=4)
Button(master, text='Login', command=) # STOPPED HERE make it login on Clicking th button
# check if correct
f = open("cards/" + f"{card_number}.cred")
lines = f.readlines()
if pin == int(lines[1]):
    print("You have successfully logged in!")
    f.close()
    # Creating a session folder
    f = open("temp", "w")
    f.write(str(card_number))
    f.write("\n")
    f.write(str(pin))
    f.close()
else:
    print("Wrong pin or card number!")
    f.close()

# session


mainloop()
