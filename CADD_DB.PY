import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="root",database="cadd_db")
cur = db.cursor(dictionary = True)
while (True):
    print("**********WELCOME TO CADD DATABASE**********".center(70))
    print("Are You Admin Or Student Choose Any one Option \n1.Admin or 2.Student")
    choice = int(input(" enter a choice :"))
    
    if choice == 1:
        email = input("enter your email id:")
        cur.execute("select * from admin")
        for i in cur:
            a=i
        B=a.get("email")
        if email in B:
            password = input("enter your password :")
            for i in cur:
                a=i
            B1=a.get("password")
            if password in B1:
                    print("Admin login successful")
                    print("1.Add Student Details")
                    print("2.Display Student Detail through id")
                    print("3.Display Student Detail Through Name ")
                    print("4.Update Student Details")
                    print("5.Delete Student Detail")
                    print("6.Display All students ")
                    # print("7.Select Specific Student")
                    choice1 = int(input("Enter Your Choice:"))
                    if choice1 == 1:
                        # Id = input(" Enter Student id :")
                        Name = input("Enter Student Name :")
                        Email = input("Enter Student Email :")
                        Password = input("Enter stuent password :")
                        Contact = int(input("Enter student conatct number :"))
                        Address = input("Enter student address :")
                        Course = input("Enter student course :")
                        Ongoing_Course = input("Enter Student Ongoing Course Name :")
                        Fees = int(input("Enter Student Fees :"))
                        Start_Date = input("Enter the student course start date :")
                        End_Date = input("Enter the student curse end date :")
                        sql = ("insert into student(name,email,password,contact,address,course,ongoing_course,fees,start_date,end_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                        var = (Name,Email,Password,Contact,Address,Course,Ongoing_Course,Fees,Start_Date,End_Date)
                        cur.execute(sql,var)
                        db.commit()
                        print(" Insert Student Record Successfull ")
                    if choice1 == 2:
                        Id = int(input(" Enter Student id : "))
                        cur.execute("select * from student where id = %s",(Id,))
                        for i in cur:
                            print(i)
                    if choice1 == 3:
                        Name = input(" Enter Student Name : ")
                        cur.execute("Select * from student where name = %s",(Name,))
                        for i in cur:
                            print(i)
                    if choice1 == 4:
                        id = int(input("enter student id for the update :"))
                        print(" 1.update Email : ")
                        print(" 2.update contact : ")
                        print(" 3.update address : ")
                        print(" 4.update course : ")
                        user_choice = int(input(" Choose any one "))
                        if user_choice == 1:
                            email = input("enter Student email :")
                            cur.execute("update student set email =  %s where id = %s",(email,id))
                        elif user_choice == 2:
                            contact = int(input("enter  student new contact number :"))
                            cur.execute("update student set contact =  %s where id = %s",(contact,id))
                        elif user_choice == 3:
                            address = input("enter student new address : ")
                            cur.execute("update student set address =  %s where id = %s",(address,id))
                        elif user_choice == 4:
                            course = input("Enter student new course : ")
                            cur.execute("update student set course =  %s where id = %s",(course,id))
                    db.commit()
                    if choice1 == 5:
                        id = int(input("enter student id for the deletion :"))
                        cur.execute("delete from student where id = %s",(id,))
                        db.commit()
                    if choice1 == 6:  
                        # id = input("enter student id for display all details : ")
                        cur.execute("select * from student ")
                        for i in cur:
                            print(i)
                        db.commit()         
            else:
                    print("Password is Incorrect")
        else:
                    print("Gmail Is Incorrect")       
    elif choice == 2:
        print("Enter Student Detail :")
        id = input("enter student id for display all details : ")
        cur.execute("select * from student where id = %s",(id,) )
        for i in cur:
            print(i)
        db.commit()
        
    
        
        
        
        
