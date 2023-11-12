import sqlite3

class PasswordDatabase:

    def __init__(self) -> None:
        self.file = './credentials.db'
        self.conn = None
        self.cur = None

    def connect_or_create(self):
        try:
            self.conn = sqlite3.connect('file:' + self.file + '?mode=rw', uri=True)
            print("connecting")
        except sqlite3.OperationalError as  err:
            print("db does not exist, creating it")
            self.conn = sqlite3.connect(self.file)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE if not exists LOGIN
                        (WEBSITE    TEXT    NOT NULL,
                         USER       TEXT    NOT NULL,
                         PASS       TEXT    NOT NULL); ''')
        #self.cur.execute("SELECT name FROM sqlite_master where type = 'table';")
        #print(self.cur.fetchall())
    
    def closeConn(self):
        if self.conn is not None:
            self.conn.close()


    def newCred(self,site,login,encrypted_password):
        self.cur.execute('INSERT INTO LOGIN VALUES(?,?,?)',[site,login,encrypted_password])

    def getCred(self,site):
        self.cur.execute('SELECT * FROM LOGIN WHERE website = ?',[site,])
        #returns a tuple
        return tuple(self.cur.fetchone())
        
        


    


#SELECT name FROM sqlite_master WHERE type='table' AND name='yourTableName';