balance = float(input("Enter opening balance: "))
number = int(input("Enter number of transactions: "))
withdrawal_limit = 10000
successful_deposits = 0
successful_withdrawals = 0
rejected = 0

for i in range(number):
    transaction_type = input("Enter transaction type (D/W): ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive")
        rejected = rejected + 1
    elif transaction_type == "D":
        balance = balance + amount
        successful_deposits = successful_deposits + 1
        print("Deposit successful")
    elif transaction_type == "W":
        if amount > withdrawal_limit:
            print("Rejected: withdrawal limit exceeded")
            rejected = rejected + 1
        elif amount > balance:
            print("Rejected: insufficient balance")
            rejected = rejected + 1
        else:
            balance = balance - amount
            successful_withdrawals = successful_withdrawals + 1
            print("Withdrawal successful")
    else:
        print("Rejected: invalid transaction type")
        rejected = rejected + 1

print("\nTRANSACTION SUMMARY")
print("Successful deposits:", successful_deposits)
print("Successful withdrawals:", successful_withdrawals)
print("Rejected transactions:", rejected)
print("Final balance: Rs.", round(balance, 2))
