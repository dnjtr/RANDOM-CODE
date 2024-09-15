class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return False  

        if self._balance < amount:
            print("Insufficient funds")
            return False  
        else:
            self._balance -= amount
            print(f"Withdrawal of ${amount} successful. Remaining balance: ${self._balance}")
            return True  
        
bankaccount = BankAccount("12345678", 1000000)
withdrawal_amount =  1000000
bankaccount.withdraw(withdrawal_amount)

