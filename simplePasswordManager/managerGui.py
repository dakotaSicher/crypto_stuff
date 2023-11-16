import tkinter as tk
import time
from PMUtils import getMaster,setMaster, getUserHash,masterExists
from PMDB import PasswordDatabase


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

class entryPopup:
    def __init__(self) -> None:
        self.window= tk.Tk()
        self.window.title("Add New Credentials")
        
        tk.Label(self.window,text="Website:").grid(row=0,column=0,sticky= 'E')
        self.site = tk.StringVar()
        tk.Entry(self.window,textvariable=self.site).grid(row=0,column=1)


        tk.Label(self.window,text="User:").grid(row=1,column=0,sticky='E')
        self.user = tk.StringVar()
        tk.Entry(self.window,textvariable=self.user).grid(row=1,column=1)

        tk.Label(self.window,text="Password:").grid(row=2,column=0,sticky='E')
        self.password = tk.StringVar()
        tk.Entry(self.window,textvariable=self.password,show='*').grid(row=2,column=1)

        tk.Button(master=self.window,text="confirm",command=self.saveCred).grid(row=3,column=0,columnspan=2)

        self.window.mainloop()

    def saveCred(self):
        self.s = self.site.get()
        self.u = self.user.get()
        self.p = self.password.get()
        print(self.s,self.u,self.p)
        self.window.destroy()


class mainView:
    def __init__(self,db) -> None:
        self.db = db

        self.window =tk.Tk()
        self.window.geometry('500x500')
        self.window.title("My password Manager")

        self.searchStr = tk.StringVar()
        tk.Button(master=self.window,text="add",command=self.addNewCred).grid(row=0,column=0,padx=2)
        tk.Entry(self.window, textvariable=self.searchStr).grid(row=0,column=2,padx=2)
        tk.Button(master=self.window,text="Find",command=self.filterView).grid(row=0,column=3,padx=2)

        tk.Label(master=self.window,text="Website:" ).grid(row=1,column=0,padx=2)
        tk.Label(master=self.window,text="username:" ).grid(row=1,column=1,padx=2)
        tk.Label(master=self.window,text="password:" ).grid(row=1,column=2,padx=2,columnspan=2)

        self.window.mainloop()

    def filterView(self):
        pass
    
    def addNewCred(self):
        addform = entryPopup()
        ep = addform.p 
        dbentry = tuple(addform.s,addform.u,ep)
        for x in dbentry:
            print(x)

        

    def deleteCred(self):
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
mydb = PasswordDatabase()
mydb.connect_or_create()
mainView(mydb)
