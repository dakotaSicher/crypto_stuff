import sqlite3

class PasswordDatabase:

    def __init__(self) -> None:
        self.file = './credentials.sqlite'
        self.conn = None
        self.cur = None

    def connect_or_create(self):
        try:
            self.conn = sqlite3.connect('file:' + self.file + '?mode=rw', uri=True)
            self.cur = self.conn.cursor()
            #self.cur.execute("SELECT name FROM sqlite_master where type = 'table';")
            #print(self.cur.fetchall())
    
        except sqlite3.OperationalError as  err:
            #print("db does not exist, creating it")
            self.conn = sqlite3.connect(self.file)
            self.cur = self.conn.cursor()
            self.cur.execute('DROP TABLE IF EXISTS LOGIN;')
            self.cur.execute('''CREATE TABLE LOGIN
                        (WEBSITE    TEXT    NOT NULL,
                         USER       TEXT    NOT NULL,
                         PASS       BLOB    NOT NULL); ''')
            #self.cur.execute("SELECT name FROM sqlite_master where type = 'table';")
            #print(self.cur.fetchall())
    
    def closeConn(self):
        if self.conn is not None:
            self.conn.close()


    def newCred(self,site,login,encrypted_password):
        self.cur.execute('INSERT INTO LOGIN VALUES(?,?,?)',[site,login,encrypted_password])
        self.conn.commit()
        print("added new cred")

    def getCred(self,site):
        self.cur.execute('SELECT * FROM LOGIN WHERE website = ?',[site,])
        #returns a tuple
        return tuple(self.cur.fetchone())
    
    def getFilteredList(self, search):
        self.cur.execute('SELECT * FROM LOGIN WHERE website like ?',['%'+search+'%',])
        #for x in self.cur:
        #    print(x)
        return self.cur.fetchall()


        
        


    


#SELECT name FROM sqlite_master WHERE type='table' AND name='yourTableName';