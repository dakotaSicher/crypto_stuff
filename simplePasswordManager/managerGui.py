import tkinter as tk
from cryptography.hazmat.primitives import hashes



class loginGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        #self.action = loginCheck

        self.Greeting = tk.Label(master=self.window, text="Welcome")
        self.Greeting.pack()
        
        self.Text = tk.Label(master=self.window,text ="Enter Master Password")
        self.Text.pack()

        self.Entry = tk.Entry(master=self.window)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Login", command=self.login)
        self.Button.pack()


    def login():
        #retrieve masterHash from file
        #hash entered password
        #compare to hash from file
        pass


class setMasterGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        #self.action = loginSet

        self.Greeting = tk.Label(master= self.window, text = "Welcome")
        self.Greeting.pack()

        self.Text = tk.Label(master=self.window, text="Enter new Master password",)
        self.Text.pack()

        self.noMatch = tk.Label(master=self.window, text = "passwords did not match, please try again")
        
        self.pwd_var = tk.StringVar()
        self.Entry = tk.Entry(master=self.window,show="*",textvariable=self.pwd_var,)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Submit", command=self.get_first)
        self.Button.pack()

        self.window.mainloop()
    
    def get_first(self):
        self.first = self.pwd_var.get()
        self.Entry.delete(0,tk.END)
        self.Button["command"] = self.get_second
        self.Text["text"] = "Confirm password"

    def get_second(self):
        self.second = self.pwd_var.get()
        if(self.second != self.first):
            self.noMatch.pack()
            self.Entry.delete(0,tk.END)
            self.Button["command"] = self.get_first
            self.Text["text"] = "Enter new Master password"
            return
      
        self.noMatch.pack_forget()
        tk.Label(master=self.window,text = "new password saved").pack()



class mainView:
    def __init__(self) -> None:
        
        self.window =tk.Tk()

        self.window.mainloop()

    def copyToClip():
        pass


setMasterGui()
