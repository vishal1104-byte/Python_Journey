#                                              A BANKING PROGRAM 

def show_balance(balance):
    print(f"Your Current Balance is: {balance:.2f} $") 

def deposit():
    amount = float(input("Enter the amount to to be deposited: ")) 
    if amount < 0:
    
        print("Thats not the valid amount ")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount You want to withdraw: "))
    if amount <= 0:
        print("You can not withdraww zero dollars from the bank ")
        return 0 
    elif amount > balance:
        print("Insufficient Balance")
        return 0 
    else:
        return amount 

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************************************")
        print("Banking Program ")
        print("*****************************************************")
        print("1. Show Balance")
        
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************************************************")

        choice = input("Enter Your choice (1-4)")

        if choice == "1":
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice")

    print("Thank You have a Nice Day ")

if __name__ == '__main__':
    main()
        