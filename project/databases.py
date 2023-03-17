import mysql.connector
class DBOperation:
    def __init__(self,database,username='root',password='',port=3308,server="localhost"):
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.server = server
        self.db = None
        try:
            self.db = mysql.connector.connect(host=self.server,user=self.username,passwd=self.password,database=self.database,port=self.port)
            print("database connection established")
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))
            print(error.errno)
            if error.errno == 1049:
                print("no such databases exists (check database spelling)")
            elif error.errno == 1045:
                print("user name is valid but password is invalid")
            elif error.errno == 2003:
                print("can not connect to mysql server (check server host name/port no) may be mysql server has not been started")
            elif error.errno == -1:
                print("no such user exists (check user spelling)")
            exit
    def FetchRow(self,sql,values=None):
        try:
            mycursor = self.db.cursor(dictionary=True)
            #execute query 
            if values==None:
                mycursor.execute(sql)
            else:
                mycursor.execute(sql,values)

            #fetch all rows
            table = mycursor.fetchall() 
            return table
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))
            print(error.errno)
            if error.errno == 1146:
                print("table does not exists")
            elif error.errno == 1054:
                print("no such field")
            elif error.errno == 1064:
                print("invalid sql query")
            return None
    def RunQuery(self,sql,values=None):
        try:
            mycursor = self.db.cursor()
            if values!=None:
                mycursor.execute(sql,values)
            else:
                mycursor.execute(sql)
        
            self.db.commit()
            print("query executed sucessfully")
            print("no of row effected ",mycursor.rowcount)
        except mysql.connector.Error as error:
            print("Something went wrong: {}".format(error))
            print(error.errno)
            if error.errno == 1146:
                print("table does not exists")
            elif error.errno == 1054:
                print("no such field")
            elif error.errno == 1064:
                print("invalid sql query")