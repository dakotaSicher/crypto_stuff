import tkinter as tk
from functools import partial
import pyperclip

from PMUtils import *
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
        self.pop.wait_window()

    def saveCred(self,event=None):
        self.s = self.siteEntry.get()
        self.u = self.userEntry.get()
        self.p = self.passwordEntry.get()
        #print(self.s,self.u,self.p)
        self.pop.after(500,self.pop.destroy)

    def genRandomPass(self):
        pass

class showPasswordPopup:
    def __init__(self,Master,pw) -> None:
        self.master= Master
        self.pop= tk.Toplevel(master=self.master)
        self.pop.title("show Passoord")
        self.pop.geometry("200x100")

        password = tk.StringVar()
        password.set(pw)
        tk.Entry(master=self.pop,textvariable=password, state="readonly" ).pack()
        self.pop.wait_window()

class mainView:
    def __init__(self,db:PasswordDatabase,key) -> None:
        self.db = db
        self.key = key

        self.window =tk.Tk()
        self.window.geometry('500x500')
        self.window.title("My password Manager")

        self.searchStr = tk.StringVar()
        self.searchStr.trace_add("write",self.filterView)
        tk.Button(master=self.window,text="add",command=self.addCred).grid(row=0,column=0,padx=2)
        tk.Entry(self.window, textvariable=self.searchStr).grid(row=0,column=2,padx=2)
        tk.Button(master=self.window,text="Find",command=self.filterView).grid(row=0,column=3,padx=2)
    
        self.viewFrame = tk.Frame(master=self.window)
        self.viewFrame.grid(row=1,column=0,columnspan=4,padx=2)
        tk.Label(master=self.viewFrame,text="Website:").grid(row=0,column=0,padx=2,sticky='W')
        tk.Label(master=self.viewFrame,text="username:" ).grid(row=0,column=1,padx=2,sticky='W')
        tk.Label(master=self.viewFrame,text="password:" ).grid(row=0,column=2,padx=2,columnspan=2,sticky="W")

        self.viewList = []
        self.viewListSite:list[tk.Text] = []
        self.viewListUser:list[tk.Entry] = []
        self.viewListPassShow:list[tk.Button] = []
        self.viewListPassCopy:list[tk.Button] = []
        self.viewListDel:list[tk.Button] = []

        self.searchStr.set("")
        self.window.mainloop()

    def filterView(self,var=None, index=None, mode=None):
        search = "{}".format(self.searchStr.get())
        #search = self.searchStr.get()
        #print(search)
        for x in self.viewListSite:
            x.destroy()
        self.viewListSite.clear()
        for x in self.viewListUser:
            x.destroy()
        self.viewListUser.clear()
        for x in self.viewListPassCopy:
            x.destroy()
        self.viewListPassCopy.clear()
        for x in self.viewListPassShow:
            x.destroy()
        self.viewListPassShow.clear()
        for x in self.viewListDel:
            x.destroy()
        self.viewListDel.clear()

        self.viewList = self.db.getFilteredList(search)
        if(len(self.viewList) == 0):
            self.viewList.append(tuple(("","","")))
            
        for x in range(len(self.viewList)):
            site = tk.StringVar()
            site.set(self.viewList[x][0])
            self.viewListSite.append(tk.Entry(master=self.viewFrame,textvariable=site,state="readonly"))
            self.viewListSite[x].grid(row=x+1,column=0,padx=2)

            user = tk.StringVar()
            user.set(self.viewList[x][1])
            self.viewListUser.append(tk.Entry(master=self.viewFrame,textvariable=user,state="readonly"))
            self.viewListUser[x].grid(row=x+1,column=1,padx=2)

            self.viewListPassShow.append(tk.Button(master=self.viewFrame,text="Show",command=partial(self.showPassword,cp=self.viewList[x][2]))) 
            self.viewListPassShow[x].grid(row=x+1,column=2,padx=2)

            self.viewListPassCopy.append(tk.Button(master=self.viewFrame,text="Copy",command=partial(self.copyToClip,cp=self.viewList[x][2]))) 
            self.viewListPassCopy[x].grid(row=x+1,column=3,padx=2)

            self.viewListDel.append(tk.Button(master=self.viewFrame,text="X",command=partial(self.deleteCred,site=self.viewList[x][0]))) 
            self.viewListDel[x].grid(row=x+1,column=4,padx=2)

    
    def addCred(self):
        addform = entryPopup(self.window)
        ep = encryptPasswords(addform.p,self.key)        
        self.db.newCred(addform.s,addform.u,ep)
        del addform
        self.filterView()
 
    def deleteCred(self, site):
        
        self.filterView()

    def copyToClip(self, cp):
        pp = decryptPasswords(cp,self.key)
        pyperclip.copy(pp)

    def showPassword(self,cp):
        pp = decryptPasswords(cp,self.key)
        showPasswordPopup(self.window,pp)


login = None
if(masterExists()):
    login = loginGui()
else:
    login = setMasterGui()
userpass = login.userpass
del login

mydb = PasswordDatabase()
mydb.connect_or_create()
key = genKeyFromMaster(userpass)

app = mainView(mydb,key)
mydb.closeConn()
