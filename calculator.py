print("**********WELCOME TO Navita's Calculator**********".center(70))
def Add(x1,x2):
    print(x1+x2)

def sub(x1,x2):
    print(x1-x2)
      
def mul(x1,x2):
    print(x1*x2)
    
def divide(x1,x2):
    print(x1%x2)
    
def mode(x1,x2):
    print(x1/x2)
    
    
print(" 1.Addition :\n 2. Substraction:\n 3. multiply :\n 4.divide :\n 5. mode :\n 6. exit ")

while True:
    x = int(input("Enter your choice:\n "))
    if x==1:
        x1 = int(input(" enter a 1st value for addition: \n "))
        x2 = int(input(" enter a 2nd value for addition : \n"))
        # Add(x1,x2) esse b aa jaega output or eche vali 2 line se b aa jaega 
        result = x1+ x2
        print(" Your addition is : " , result)
        
    elif x==2:
        x1 = int(input(" enter a 1st value for subtartion: \n"))
        x2 = int(input(" enter a 2nd value for subtartion: \n"))
        sub(x1,x2)
        
    elif x==3:
    
        x1 = int(input(" enter a 1st value for multiply: \n "))
        x2 = int(input(" enter a 2nd value for multiply: \n "))
        mul(x1,x2)
    
    elif x==4:
        x1 = int(input(" enter a 1st value for divide : \n"))
        x2 = int(input(" enter a 2nd value for divide : \n"))
        divide(x1,x2)
    
    elif x==5:
        x1 = int(input(" enter a 1st value for mode : \n"))
        x2 = int(input(" enter a 2nd value for mode : \n"))
        mode(x1,x2)
        
    elif x==6:
        print("exit")
        break
    else:
        print(" Invalid choice ")
        
    next_input = input(" Do you want to continue:? yes/no  \n ")
    if next_input == "yes":
        continue
    elif next_input == "no":
        break
        
    else:
        print("Invalid Choice")
 






