import mysql.connector
db = mysql.connector.connect(host = "localhost",password = "root",user = "root",database = "navita")
cur = db.cursor()
print(" Enter For The 1. Registration Or 2. Login Page ")
while (True):
    Choice = int(input(" Enter your choice : "))   
    if Choice == 1:
        Name = input(" Enter a name : ")
        Contact = int(input(" Enter a contact number : ")) 
        Gmail = input(" Enter a gmail Id : ")
        Salary = int(input(" Enter a salary amount : "))   
        Adders = input(" Enter a address :")
        Password = int(input(" Enter a password : "))
        cur.execute("insert into Registration (name,contact,gmail,salary,adders,password) values (%s,%s,%s,%s,%s,%s)",(Name,Contact,Gmail,Salary,Adders,Password))
        db.commit()
        print("Registration successful")
    elif Choice == 2:
        gmail = input(" enter your Gmail : ")
        Password = input(" enter your password ")
        cur.execute("select Gmail,Password,ID,Name,Contact,salary,Adders from Registration where gmail = %s",(gmail,))
        for i in cur:
            print(i)
            if gmail and Password in i:
                print("login successfull")
            else:
                print("Login Unsuccessfull Please Try Again Later")        