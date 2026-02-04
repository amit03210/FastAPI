"""
Bank App
"""

# Custom Exception
class InsufficientBalanceError(Exception):
    pass
# ---------------
# Account Logic
# ---------------

def deposit(balance, amount):
    balance += amount
    f = open("1. Python refresher\\14. Errors and Exception\\bank_app\\transactions.txt", "a")
    f.write(f"deposit, {amount}\n")
    f.close();
    print("Depsoit sucessfull")
    return balance

def withdraw(balance, amount):
    if amount>balance:
        raise InsufficientBalanceError
    balance -= amount
    with open("1. Python refresher\\14. Errors and Exception\\bank_app\\transactions.txt", "a") as f:
        f.write(f"Withdraw, {amount}\n")
    print("Amount withrawn, please collect your cash")
    return balance
    

def read_transaction():
    with open("1. Python refresher\\14. Errors and Exception\\bank_app\\transactions.txt", "r") as f:
      for lines in f:
        print(lines)  

def service_request()->int:
            print("Enter valid service number")
            service = int(input("1. Deposit\n2. Withdrawal\n3. Check Balance\n5. Read Transactions\n4. Exit\n"))
            while(service != 1 and service != 2 and service != 3 and service != 4 and service != 5):
                print("Please choose valid service number")
                service = int(input("1. Deposit\n2. Withdrawal\n3. Check Balance\n4. Exit\n"))
            return service

def main():
    balance = 1500

    try:
        print("Select number for the Service: ")
        service = service_request()

        match service:
            case 1: 
                print("You selected Deposit request.")
                amount = int(input("Enter amount: "))
                balance = deposit(balance, amount)
            case 2:
                print("You selected Withrawal request.")
                amount = int(input("Enter amount: "))
                balance = withdraw(balance, amount)
            case 3: 
                print("You selected option to check balance of your account.")
                print("Your current balance is", balance)
            case 5:
                print("Your bank records")
                read_transaction()
            case 4:
                print("Thank you for your patience")
                return;

    except ValueError:
        f = open("1. Python refresher\\14. Errors and Exception\\bank_app\\error_log.txt", "w")
        f.write("Please enter valid number")
        print("Please enter valid number")
        f.close();        

    except InsufficientBalanceError:
        print("Oops you do not have enough balance.")
    
    finally:
        print(f"Your final balance is {balance}")

if __name__ == "__main__":
    main()
