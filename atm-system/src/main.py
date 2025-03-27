from atm import ATM

def display_menu():
    print("\n===== ATM =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. History")
    print("6. List Accounts")
    print("0. Exit")
    return input("Choice: ")

def main():
    atm = ATM()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            account_id = input("Account ID: ")
            try:
                balance = float(input("Initial balance: "))
                if balance < 0:
                    print("Cannot be negative")
                    continue
            except ValueError:
                print("Invalid amount")
                continue
                
            if atm.create_account(account_id, balance):
                print(f"Account created!")
            else:
                print(f"Account already exists")
        
        elif choice == '2':
            account_id = input("Account ID: ")
            balance = atm.get_balance(account_id)
            
            if balance is not None:
                print(f"Balance: ${balance:.2f}")
            else:
                print("Account not found")
        
        elif choice == '3':
            account_id = input("Account ID: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount")
                continue
                
            if atm.deposit(account_id, amount):
                print(f"${amount:.2f} deposited")
                print(f"New balance: ${atm.get_balance(account_id):.2f}")
            else:
                print("Deposit failed")
        
        elif choice == '4':
            account_id = input("Account ID: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount")
                continue
                
            if atm.withdraw(account_id, amount):
                print(f"${amount:.2f} withdrawn")
                print(f"New balance: ${atm.get_balance(account_id):.2f}")
            else:
                print("Withdrawal failed")
        
        elif choice == '5':
            account_id = input("Account ID: ")
            transactions = atm.get_transactions(account_id)
            
            if transactions is not None:
                if not transactions:
                    print("No transactions")
                else:
                    for i, t in enumerate(transactions, 1):
                        print(f"{i}. {t['type']}: ${t['amount']:.2f}")
            else:
                print("Account not found")
        
        elif choice == '6':
            accounts = atm.get_accounts()
            
            if not accounts:
                print("No accounts")
            else:
                for acc_id, data in accounts.items():
                    print(f"{acc_id}: ${data['balance']:.2f}")
        
        elif choice == '0':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
