import databases as mydb
import datetime
import common_function as cf 
from datetime import datetime

db = mydb.DBOperation("py11")
def DisplayProduct():
    sql = "select * from product order by name"
    table = db.FetchRow(sql)
    print(f"{'':8}{'id':2}|{'name':33}{'detail':69}{'price':17}{'stock':12}")
    print("-"*140)
    for row in table:
        output = f"{row['id']:10} {row['name']:32} {row['detail']:55} {row['price']:17} {row['stock']:12}"
        print(output)
def DisplayBill(sql,data):
    table = db.FetchRow(sql,data)
    flag = ['Credit','Cash']
    print(f"{'':8}{'id':2}|{'customername':64}{'bill date':30}{'amount':8}{'sale type':10}")
    print("-"*140)
    for row in table:
        mydate = cf.ConvertToDMY(row['billdate'])
        output = f"{row['id']:10} {row['customername']:64} {mydate:20} {row['amount']:15} {flag[row['iscash']]:10}"
        print(output)
def Bill():
    sql = None
    ModuleChoice=-1
    while ModuleChoice!=0:
        print("Press 1 for product management")
        print("Press 2 for bill management")
        print("Press 0 for exit ")
        ModuleChoice = int(input("Enter your choice"))
        if ModuleChoice==1:
            ProductChoice=-1
            while ProductChoice!=0:
                print("press 1 to add new product ")
                print("press 2 to delete existing product ")
                print("press 3 to edit product ")
                print("press 4 to view product ")
                print("press 0 to exit to main menu ")
                ProductChoice = int(input("Enter your choice"))
                if ProductChoice==1:
                    name = input('enter product name')
                    detail = input('enter product detail')
                    price = int(input('enter product price'))
                    stock = int(input('enter product quantity'))
                    sql = "insert into product(name,detail,price,stock) values (%s,%s,%s,%s)";
                    data = [name,detail,price,stock]
                    db.RunQuery(sql,data)
                    print("Product added")
                elif ProductChoice==2:
                    DisplayProduct()
                    id = int(input("Enter product id"))
                    sql = "delete from product where id=%s"
                    data = [id]
                    db.RunQuery(sql,data)
                    print("Product deleted")
                elif ProductChoice==3:
                    DisplayProduct()
                    productid = int(input("Enter product id"))
                    sql = "select id from product where id=%s"
                    data = [productid]
                    table = db.FetchRow(sql,data)
                    size = len(table)
                    if size == 0:
                        print("product not found")
                    else:
                        name = input('enter product name')
                        detail = input('enter product detail')
                        price = int(input('enter product price'))
                        stock = int(input('enter product quantity'))
                        sql = "update product set name=%s,price=%s,stock=%s,detail=%s where id=%s"
                        data = [name,price,stock,detail,productid]
                        db.RunQuery(sql,data)
                        print("Product updated....")
                        
                elif ProductChoice==4:
                    DisplayProduct()
                elif ProductChoice==0:
                    print("exit to main menu")
                else:
                    print("invalid choice for product management")    
        elif ModuleChoice==2:
            BillChoice = -1
            while BillChoice!=0:
                print(" press 1 to add product into bill ")
                print(" press 2 to delete  product from bill ")
                print(" press 3 to view bill items ")
                print(" press 4 to save and print bill ")
                print(" press 5 to get details of bill between given date ")
                print(" press 6 to search for specific bill by name")
                print("press  0 to exit to main menu ")
                BillChoice = int(input("Enter your choice"))
                if BillChoice==1:
                    DisplayProduct()
                    productid = int(input("Enter product id"))
                    sql = "select price,stock from product where id=%s"
                    data = [productid]
                    table = db.FetchRow(sql,data)
                    size = len(table)
                    if size == 0:
                        print("product not found")
                    else:
                        print("Product found")
                        for row in table:
                            stock = row['stock']
                            price = row['price']
                        quantity = int(input("Enter quantity"))
                        if quantity>stock:
                            print("not enough stock")
                        else:
                            sql = "insert into bill_product (productid,quantity,price,billid) values (%s,%s,%s,%s)"
                            data = [productid,quantity,price,0]
                            db.RunQuery(sql,data)
                            
                            sql = "update product set stock=stock-%s where id=%s"
                            data = [quantity,productid]
                            db.RunQuery(sql,data)
                            print("product added into bill")
                            
                elif BillChoice==2:
                    DisplayProduct()
                    productid = int(input("Enter product id"))
                    sql = "select price,stock from product where id=%s"
                    data = [productid]
                    table = db.FetchRow(sql,data)
                    size = len(table)
                    if size == 0:
                        print("product not found")
                    else:
                        print("Product found")
                        sql = "select quantity from bill_product where productid=%s and billid=%s"
                        data = [productid,0]
                        table2 = db.FetchRow(sql,data)
                        for row in table2:
                            quantity = row['quantity']
                        
                        sql = "update product set stock=stock+%s where id=%s"
                        data = [quantity,productid]
                        db.RunQuery(sql,data)
                        
                        sql = "delete from bill_product where productid=%s and billid=%s"
                        data = [productid,0]
                        db.RunQuery(sql,data)
                        print("product removed from bill")
                        
                elif BillChoice==3:
                    sql = "select p.id as id,quantity,b.price as price ,name from bill_product as b, product as p where b.productid=p.id and billid=%s"
                    data = [0]
                    table = db.FetchRow(sql,data)
                    print(f"{'':8}{'id':2}|{'name':43}{'price':17}{'quantity':12}")
                    print("-"*140)
                    billtotal=0
                    for row in table:
                        output = f"{row['id']:10} {row['name']:32}{row['price']:17} {row['quantity']:12}"
                        print(output)
                        billtotal += row['price']  * row['quantity']
                    print("-"*140)
                    print(f"Grand Total = {'':39}",billtotal)
                elif BillChoice==4:
                    print("here we will save and print bill")
                    #check is there any pending product in bill_product table or not
                    sql = "select id from bill_product where billid=%s"
                    data = [0]
                    table = db.FetchRow(sql,data)
                    size = len(table)
                    print(size)
                    if size==0:
                        print("no product found in bill")
                    else:
                        customername = input("Enter buyer name")
                        email = input("Enter buyer email address")
                        print("Press 1 for cash bill")
                        print("Press 0 for credit bill")
                        iscash = int(input("enter your choice"))
                        sql = "SELECT sum(quantity*price) as total FROM `bill_product` where billid=%s"
                        data = [0]
                        table = db.FetchRow(sql,data)
                        for row in table:
                            total = row['total']
                        print(total)
                        CurrentDate = datetime.date.today() #return date in YYYY-MM-DD
                        print(CurrentDate)
                        sql = "insert into bill (customername,billdate,amount,iscash,email) values(%s,%s,%s,%s,%s)"
                        data = [customername,CurrentDate,total,iscash,email]
                        db.RunQuery(sql,data)
                        sql = "SELECT max(id) as last_bill_id FROM `bill`"
                        table = db.FetchRow(sql)
                        for row in table:
                            last_bill_id = row['last_bill_id']
                        sql ="update bill_product set billid=%s where billid=%s"
                        data = [last_bill_id,0]
                        db.RunQuery(sql,data)
                        print("Bill Saved successfully")
                elif BillChoice==5:
                    print("here we will get details of bill between given date  ")
                    sql = "SELECT * FROM `bill` WHERE date(`billdate`)>=%s and date(`billdate`)<=%s"
                    startdate = input("Enter bill start date (dd-mm-YYYY)")
                    enddate = input("Enter bill end date (dd-mm-YYYY)")
                    startdate = datetime.strptime(startdate,"%d-%m-%Y").strftime("%Y-%m-%d")
                    enddate = datetime.strptime(enddate,"%d-%m-%Y").strftime("%Y-%m-%d")
                    data = [startdate,enddate] 
                    DisplayBill(sql,data)
                elif BillChoice==6:
                    name = input("Enter customer name")
                    sql = "select * from bill where customername like %s order by id desc"
                    name = f"%{name}%"
                    data = [name]
                    DisplayBill(sql,data)
                elif BillChoice==0:
                    print("exit to main menu")   
                else:
                    print("invalid choice for bill management")   
        elif ModuleChoice==0:
            print("Good bye....")
            return 
        else:
            print("invalid choice")
Bill()