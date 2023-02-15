import connection as con 
name = input("Enter book name")
author = input("Enter author name")
price = int(input("Enter price"))
mycursor = con.db.cursor()
#create query 
sql = "insert into book (name,author,price) values (%s,%s,%s)"
#create list of size 3
values = [name,author,price]
mycursor.execute(sql,values)
con.db.commit()
print("Book Added...")