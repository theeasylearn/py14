import databases as mydb
db = mydb.DBOperation("py11")
def Bill():
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
                    print("here we will add new product")
                elif ProductChoice==2:
                    print("here we will delete product")
                elif ProductChoice==3:
                    print("here we will edit product")
                elif ProductChoice==4:
                    print("here we will view product")
                elif ProductChoice==0:
                    print("exit to main menu")
                else:
                    print("invalid choice for product management")    
        elif ModuleChoice==2:
            BillChoice = -1
            while BillChoice!=0:
                print(" press to add product into bill ")
                print(" press to delete  product from bill ")
                print(" press to view bill items ")
                print(" press to save and print bill ")
                print(" press to get details of bill between given date ")
                print(" press to search for specific bill by name")
                print("press 0 to exit to main menu ")
                BillChoice = int(input("Enter your choice"))
                if BillChoice==1:
                    print("here we will add product into bill")
                elif BillChoice==2:
                    print("here we will delete product from bill")
                elif BillChoice==3:
                    print("here we will view product of bill")
                elif BillChoice==4:
                    print("here we will save and print bill")
                elif BillChoice==5:
                    print("here we will get details of bill between given date  ")
                elif BillChoice==6:
                    print("here we will  search for specific bill by name")
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