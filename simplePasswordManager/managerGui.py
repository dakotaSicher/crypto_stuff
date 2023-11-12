import tkinter as tk

class loginGui:
    def __init__(self, loginCheck) -> None:
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
    def __init__(self, loginSet) -> None:
        self.window = tk.Tk()
        #self.action = loginSet

        self.Greeting = tk.Label(master= self.window, text = "Welcome")
        self.Greeting.pack()

        self.Text1 = tk.Label(master=self.window, text="Enter new Master password")
        self.Text1.pack()

        self.Text2 = tk.Label(master=self.window, text="Confrim new master password")
        self.noMatch = tk.Label(master=self.window, text = "passwords did not match, please try again")

        self.Entry = tk.Entry(master=self.window)
        self.Entry.pack()

        self.Button = tk.Button(master=self.window,text="Submit", command=self.setMaster)
        self.Button.pack()

        self.window.mainloop()
    
    def setMaster():
        #accept first entry
        #accept second entry
        #compare first and second 
        #repeate if not matching
        #once matching, hash and store
        pass


class mainView:
    def __init__(self) -> None:
        
        self.window =tk.Tk()

        self.window.mainloop()

    def copyToClip():
        pass