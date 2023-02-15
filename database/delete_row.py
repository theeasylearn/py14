import connection as con 
id = int(input("Enter book id to delete book"))
#create cursor 
mycursor = con.db.cursor()

#create query 
sql = "delete from book where id=%s"

#create list of size 1
values = [id]
mycursor.execute(sql,values)
con.db.commit()
if mycursor.rowcount>=1:
    print("book deleted....")
else:
    print("Id not found")