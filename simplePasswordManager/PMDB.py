import sqlite3
from os import path

#Handles all direct interactions with the database
class PasswordDatabase:

    def __init__(self) -> None:
        dirname = path.dirname(__file__)
        self.file = path.join(dirname,'sicherDB.sqlite')
        self.conn = None
        self.cur = None

    #Connects to an exsisting database file
    #or creates the file and sets up the db schema
    def connect_or_create(self):
        try:
            self.conn = sqlite3.connect('file:' + self.file + '?mode=rw', uri=True)
            self.cur = self.conn.cursor()
            #self.cur.execute("SELECT name FROM sqlite_master where type = 'table';")
            #print(self.cur.fetchall())   
        except sqlite3.OperationalError:
            self.conn = sqlite3.connect(self.file)
            self.cur = self.conn.cursor()
            self.cur.execute('DROP TABLE IF EXISTS LOGIN;')
            self.cur.execute('''CREATE TABLE LOGIN
                        (WEBSITE    TEXT    NOT NULL,           
                         USER       TEXT    NOT NULL,
                         PASS       BLOB    NOT NULL); ''')

    def closeConn(self):
        if self.conn is not None:
            self.conn.close()

    #Database access and modification functions using prepared statements from sqlite
    ##########################################################################
    def newCred(self,site,login,encrypted_password):
        self.cur.execute('INSERT INTO LOGIN VALUES(?,?,?)',[site,login,encrypted_password])
        self.conn.commit()
        print("added new cred")

    def delCred(self,site):
        self.cur.execute('DELETE FROM LOGIN WHERE website = ?',[site,])
        self.conn.commit()

    def getCred(self,site):
        self.cur.execute('SELECT * FROM LOGIN WHERE website = ?',[site,])
        return tuple(self.cur.fetchone())
    
    #q
    def getFilteredList(self, search):
        self.cur.execute('SELECT * FROM LOGIN WHERE website like ?',['%'+search+'%',])
        return self.cur.fetchall()


#SELECT name FROM sqlite_master WHERE type='table' AND name='yourTableName';