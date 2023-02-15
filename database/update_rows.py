import connection as con 

id = int(input("enter book id to update book"))
name = input("enter book name")
author = input("enter author name")
price = int(input("enter price "))

# create cursor 
mycursor = con.db.cursor()

#create query 
sql = "update book set name=%s,author=%s,price=%s where id=%s"

#create list 
values = [name,author,price,id]

#execute query
mycursor.execute(sql,values)

con.db.commit()

if mycursor.rowcount>=1:
    print("Book updated")
else:
    print("ID not found")
    
    