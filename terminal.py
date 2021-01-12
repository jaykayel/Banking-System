from tkinter import *
import newcard
import keygen
import login

class Terminal:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        # Create Account
        self.create = Button(frame,
                             text="Create Account",
                             command=self.create)
        self.create.pack(side=TOP)
        # Login
        self.login = Button(frame,
                             text="Login",
                             command=self.login)
        self.login.pack(side=TOP)
        # Leave Terminal
        self.button = Button(frame,
                             text="Leave Terminal", fg="red",
                             command=frame.quit)
        self.button.pack(side=BOTTOM)



    def create(self):
        newcard.Create()
        keygen.generate()
        login.Login()

    def login(self):
        login.Login()

    def leave(self):
        exit()

root = Tk()
app = Terminal(root)
root.mainloop()