
balance = 100000
pin = 1234

while True:
    print("\n")
    print("Welcome to Navita's Bank".center(90))
    print("*"*100)
    print("🏦 MENU OPTIONS".center(90))
    print("1.Check Balance".center(90))
    print("2. Withdrawal".center(90))
    print("3. Deposit".center(90))
    print("4. Change Pin".center(90))
    print("5. EXIT".center(90))
    print("*"*100)

    n = input("\nEnter Your Choice: ")

    if n == "1":
        K = int(input("Enter pin: "))
        if pin == K:
            print("\n📊 Your Balance is: $", balance)
        else:
            print("\n❌ Invalid pin")
    elif n == "2":
        K = int(input("Enter pin: "))
        if pin == K:
            withdraw = int(input("Enter withdrawal amount: $"))
            if balance >= withdraw:
                balance -= withdraw
                print("\n💸 Withdrawal successful!")
                print("💰 New Balance: $", balance)
            else:
                print("\n❌ Insufficient funds for withdrawal!")
        else:
            print("\n❌ INVALID PIN")
    elif n == "3":
        K = int(input("Enter pin: "))
        if pin == K:
            deposit = int(input("Enter deposit amount: $"))
            balance += deposit
            print("\n💰 Deposit successful!")
            print("💰 Total Balance: $", balance)
        else:
            print("\n❌ INVALID PIN")
    elif n == "4":
        K = int(input("Enter pin: "))
        if pin == K:
            newpin = int(input("Enter new pin: "))
            pin = newpin
            print("\n🔐 Pin changed successfully")
        else:
            print("\n❌ Incorrect PIN. Try again")
    elif n == "5":
        print("\n👋 Exited")
        break

print("\nThank you for using Navita's Bank! Have a Great Day!")
