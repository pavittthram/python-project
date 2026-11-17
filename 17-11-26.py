balance = 5000
pin = input("Enter PIN: ")

if pin == "1234":
    while True:
        print("1.Balance 2.Deposit 3.Withdraw 4.Exit")
        choice = input("Choose (1-4): ")
        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = int(input("Deposit amount: "))
            balance = balance + amount
            print("New Balance:", balance)
        elif choice == "3":
            amount = int(input("Withdraw amount: "))
            if amount <= balance:
                balance = balance - amount
                print("Remaining Balance:", balance)
            else:
                print("Insufficient balance")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
else:
    print("Wrong password")