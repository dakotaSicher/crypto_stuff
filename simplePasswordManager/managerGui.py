import tkinter as tk
#from cryptography.hazmat.primitives import hashes
import time
from passwordManager import getMaster,setMaster, getUserHash,masterExists



class loginGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("LOGIN")
        self.window.geometry('250x100')

        self.Greeting = tk.Label(master=self.window, text="Welcome")
        self.Greeting.pack()
        
        self.Text = tk.Label(master=self.window,text ="Enter Master Password")
        self.Text.pack()

        self.pwd_var = tk.StringVar()
        self.Entry = tk.Entry(master=self.window,show="*",textvariable=self.pwd_var,)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Login", command=self.login)
        self.Button.pack()

        self.noMatch = tk.Label(master=self.window, text = "password is incorrect, try again")

        self.masterHash = getMaster()
        self.window.mainloop()

    def login(self):
        self.userpass = self.pwd_var.get()
        self.userhash = getUserHash(self.userpass)
        if(self.userhash != self.masterHash):
            self.noMatch.pack()
            self.Entry.delete(0,tk.END)
        else:
            self.noMatch.pack_forget()
            tk.Label(master=self.window,text = "success").pack()
            time.sleep(1)
            self.window.destroy()


        #retrieve masterHash from file
        #hash entered password
        #compare to hash from file
        pass


class setMasterGui:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("New Passoword")
        self.window.geometry('250x100')

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
        else:
            self.noMatch.pack_forget()
            tk.Label(master=self.window,text = "new password saved").pack()
            setMaster(self.second)
            self.userpass = self.second
            time.sleep(1)
            self.window.destroy()



class mainView:
    def __init__(self) -> None:
        
        self.window =tk.Tk()
        self.window.geometry('500x500')
        self.window.title("My password Manager")
        self.window.mainloop()

    def filterView():
        pass

    def copyToClip():
        pass

    def showPassword():
        pass



login = None
if(masterExists()):
    login = loginGui()
else:
    login = setMasterGui()
userpass = login.userpass
del login
print("login success")
mainView()
