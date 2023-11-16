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
        self.Entry = tk.Entry(master=self.window,show="*",textvariable=self.pwd_var)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Login", command=self.login)
        self.Button.pack()

        self.noMatch = tk.Label(master=self.window, text = "password is incorrect, try again")

        self.Entry.bind("<Return>", self.login)
        self.masterHash = getMaster()
        self.window.mainloop()

    def login(self, event=None):
        self.userpass = self.pwd_var.get()
        self.userhash = getUserHash(self.userpass)
        if(self.userhash != self.masterHash):
            self.noMatch.pack()
            self.Entry.delete(0,tk.END)
        else:
            self.noMatch.pack_forget()
            tk.Label(master=self.window,text = "success").pack()
            self.window.after(1000,self.window.destroy)


        #retrieve masterHash from file
        #hash entered password
        #compare to hash from file



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
        self.Entry = tk.Entry(master=self.window,show="*",textvariable=self.pwd_var)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Submit", command=self.get_first)
        self.Button.pack()

        self.Entry.bind("<Return>", self.get_first)
        self.window.mainloop()
    
    def get_first(self,event=None):
        self.first = self.pwd_var.get()
        self.Entry.delete(0,tk.END)
        self.Button["command"] = self.get_second
        self.Entry.bind("<Return>", self.get_second)
        self.Text["text"] = "Confirm password"

    def get_second(self,event=None):
        self.second = self.pwd_var.get()
        if(self.second != self.first):
            self.noMatch.pack()
            self.Entry.delete(0,tk.END)
            self.Button["command"] = self.get_first
            self.Entry.bind("<Return>", self.get_first)
            self.Text["text"] = "Enter new Master password"
        else:
            self.noMatch.pack_forget()
            tk.Label(master=self.window,text = "new password saved").pack()
            setMaster(self.second)
            self.userpass = self.second
            self.window.after(1000,self.window.destroy)


class entryPopup:
    def __init__(self,Master) -> None:
        self.master= Master
        self.pop= tk.Toplevel(master=self.master)
        self.pop.title("Add New Credentials")
        self.pop.geometry("200x100")
        
        tk.Label(master=self.pop,text="Website:").grid(row=0,column=0,sticky= 'E')
        self.site = tk.StringVar()
        self.siteEntry = tk.Entry(master=self.pop,textvariable=self.site)
        self.siteEntry.grid(row=0,column=1)


        tk.Label(master=self.pop,text="User:").grid(row=1,column=0,sticky='E')
        self.user = tk.StringVar()
        self.userEntry = tk.Entry(master=self.pop,textvariable=self.user)
        self.userEntry.grid(row=1,column=1)

        tk.Label(master=self.pop,text="Password:").grid(row=2,column=0,sticky='E')
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(master=self.pop,show='*',textvariable=self.password)
        self.passwordEntry.grid(row=2,column=1)

        tk.Button(master=self.pop,text="confirm",command=self.saveCred).grid(row=3,column=0,columnspan=2)

        self.pop.bind("<Return>", self.saveCred)
        #self.pop.mainloop()

    def saveCred(self,event=None):
        print(self.site.get(),self.user.get(),self.password.get())
        self.s = self.siteEntry.get()
        self.u = self.userEntry.get()
        self.p = self.passwordEntry.get()
        #print(self.s,self.u,self.p)
        self.pop.after(500,self.pop.destroy)

    def genRandomPass(self):
        pass


class mainView:
    def __init__(self,db) -> None:
        self.db = db

        self.window =tk.Tk()
        self.window.geometry('500x500')
        self.window.title("My password Manager")

        self.searchStr = tk.StringVar()
        self.searchStr.trace_add("write",self.filterView)
        tk.Button(master=self.window,text="add",command=self.addNewCred).grid(row=0,column=0,padx=2)
        tk.Entry(self.window, textvariable=self.searchStr).grid(row=0,column=2,padx=2)
        tk.Button(master=self.window,text="Find",command=self.filterView).grid(row=0,column=3,padx=2)

        tk.Label(master=self.window,text="Website:" ).grid(row=1,column=0,padx=2)
        tk.Label(master=self.window,text="username:" ).grid(row=1,column=1,padx=2)
        tk.Label(master=self.window,text="password:" ).grid(row=1,column=2,padx=2,columnspan=2)

        self.window.mainloop()

    def filterView(self,var,index,mode):
        search = "{}".format(self.searchStr.get())
        print(search)
        self.displayList = self.db.getFilteredList(search)
        print(self.displayList)
        pass
    
    def addNewCred(self):

        self.addform = entryPopup(self.window)
        print("im back")
        print(self.addform.s)
        del self.addform

 
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
print(userpass)
del login
#print("login success")
mydb = PasswordDatabase()
mydb.connect_or_create()
app = mainView(mydb)
