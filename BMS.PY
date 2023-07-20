import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="root",database="BMS")
cur = db.cursor()
# Balance = 5000
for i in range (0,9999):
    print ("********** Welcome TO Navita's Bank **********".center(70))
    print("MAINMENU".center(65))
    print(" 1 .Insert Record /Records".center(65))
    print(" 2.Display Records As Per The Account_No./Contact_No".center(65) )
    print(" 3.Search Record Details as per the Account Number: ".center(65))
    print(" 4. Update Reocrd : ".center(60))
    print(" 5.Delete Record : ".center(60))
    print(" 6. Transactins Debit\Withraw from the account: ".center(65))
    # print("a.Debit/Withraw from the Account".center(65))
    # print("b.Credit into the Account_No".center(65))
    print("7.Exit".center(65))
    
    choice = int(input(" enter a choice :"))
    if choice == 1:
        account_no = int(input(" enter a account_no.:" ))
        ifsc_code = int(input(" enter a ifsc code: " ))
        name = input("enter a name:")
        contact_no = int(input("enter a contact no:"))
        address = (input("enter a address:"))
        gmail_id = (input("enter a gmail id:"))
        password = int(input("Enter a password:"))
        Balance = int(input(" Enter A Balance "))
        sql = ("insert into records(account_no,name,address,ifsc_code,contact,gmail_id,Balance,password) values (%s,%s,%s,%s,%s,%s,%s,%s)")
        var = (account_no,name,address,ifsc_code,contact_no,gmail_id,Balance,password)
        cur.execute(sql,var)
        db.commit()
        print(" Insert Record Successfull ")
    elif choice == 2:
        print("a.sorted as per account_no:") 
        print("b.sorted as per contact Number:")
        print("c.sorted as per customer Ifsc code:")
        choice2 = input(" Enter a Option :")
        if choice2 == 'a':
            account_no = int(input("Enter a account "))
            cur.execute("select * from records where account_no = %s",(account_no,))
            for i in cur:
                print(i)
        elif choice2 == 'b':
            contact = int(input(" Enter a contact:"))
            cur.execute("select * from records where contact = %s",(contact,))
            for i in cur:
                print(i)
        elif choice2 == 'c':
            ifsc_code = int(input(" Enter a ifsc_code :"))
            cur.execute("Select * from records where ifsc_code = %s",(ifsc_code,))
            for i in cur:
                print(i)
    elif choice == 3:
        account_no = int(input("Enter a account "))
        cur.execute("select * from records where account_no = %s",(account_no,))
        for i in cur:
            print(i)     
    elif choice == 4:
        account_no = int(input("Enter user account no for the Update :"))
        print(" a.Update Name :")
        print(" b.Update Contact_No. :")
        print(" c.Update Address :")
        print(" d.Update Gmail ID :")
        user_choice = input("Enter a Above Mention Choice :")
        if user_choice == 'a':
            name = input(" enter a new name : ")
            cur.execute("update records set name = %s where account_no = %s",(name,account_no,))
            db.commit()   
        elif user_choice == 'b':
            contact = int(input(" Enter a new contact number "))
            cur.execute("update records set contact = %s where account_no = %s",(contact,account_no))
            db.commit() 
        elif user_choice == 'c':
            address = input(" Enter a new address : ")
            cur.execute("update records set address = %s where account_no = %s",(address,account_no,))
            db.commit()  
        elif user_choice == 'd':
            gmail_id = input("enter a new Gmail Id :")
            cur.execute("update records set gmail_id = %s where account_no = %s",(gmail_id,account_no,))
            db.commit()
    elif choice == 5:
        account_no = int(input("Enter user account no for the Delete :"))
        cur.execute("Delete from records where account_no = %s",(account_no,))
        db.commit()
        print("Subject Account Delete Successfully")
    elif choice == 6:
        account_no = int(input("Enter user account no for the Debit/Withdraw/Credit:"))
        print("a. Debit/Withdraw from the Account")
        print("b. Credit into the Account_No")
        user_choice = input("Enter A Above Mentioned Choice: ")
        if user_choice == 'a':
            account_no = int(input("ENTER YOUR ACCOUNT NUMBER:"))
            cur.execute("SELECT ACCOUNT_NO from records WHERE ACCOUNT_NO=%s", (account_no,))
            for i in cur:
                if account_no in i:
                    withdraw = int(input("ENTER AMOUNT TO WITHDRAW ="))
                    cur.execute("SELECT balance FROM records WHERE ACCOUNT_NO=%s", (account_no,))
                    for j in cur:
                        if withdraw > j[0]:
                            print("INSUFFICIENT BALANCE")
                            break
                        else:
                            total = j[0] - withdraw
                            print("Available Balance is: ₹", total)
                            cur.execute("UPDATE records SET BALANCE=%s WHERE ACCOUNT_NO=%s", (total, account_no))
                            db.commit()
                            print("WITHDRAWAL SUCCESSFUL")
                else:
                    print("INCORRECT CREDENTIALS")
        elif user_choice == 'b':
            account_no = int(input("ENTER YOUR ACCOUNT NUMBER:"))
            passwd = int(input("ENTER YOUR PASSWORD:"))
            cur.execute("SELECT ACCOUNT_NO, PASSWORD FROM records WHERE ACCOUNT_NO=%s", (account_no,))
            record = cur.fetchone()
            if record and record[1] == passwd:
                credit = int(input("ENTER AMOUNT TO DEPOSIT ="))
                cur.execute("SELECT balance FROM records WHERE ACCOUNT_NO=%s", (account_no,))
                balance_row = cur.fetchone()
                if balance_row is not None:
                    balance = balance_row[0]
                    total = balance + credit
                    print("New Balance:", total)
                    cur.execute("UPDATE records SET BALANCE=%s WHERE ACCOUNT_NO=%s", (total, account_no))
                    db.commit()
                    print("CREDITED SUCCESSFUL")
                else:
                    print("Account number not found in the database.")
            else:
                print("INCORRECT CREDENTIALS")
    elif choice == 7:
        print("THANK YOU FOR VISITING IN MY BANK ".center(65))
        print("Exiting the Bank Application")
        break
    
        
    
       
            
             
        
    
        
        