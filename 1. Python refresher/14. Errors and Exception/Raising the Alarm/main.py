# Create a function 'withdraw_money(amount, balance)'.
# If 'amount' is greater than 'balance', 'raise' a PermissionError 
# with the message "Insufficient funds". 
# Test it by calling the function inside a try-except block.

# class PermissionError(Exception):
#     print("Insufficent funds.")

def withdraw_money(amount, balance):
    if (amount>balance):
        raise PermissionError("Insufficent Funds.")
    else:
        balance = balance - amount
        print("Withdraw Sucessfully.")

if __name__ == "__main__":
    try:
        withdraw_money(11, 10)
    except PermissionError as e:
        print(e)