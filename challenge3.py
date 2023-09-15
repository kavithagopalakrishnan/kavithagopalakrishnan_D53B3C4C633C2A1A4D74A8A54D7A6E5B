class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited{amount}. New balance: {self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew{amount}. New balance: {self.__account_balance}"
        else:
            return "Withdrawal amount exceeds account balance or is invalid."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: {self.__account_balance}"
if __name__ == "__main__":
    my_account = BankAccount("1234567890", "hari", 1000)
    print(my_account.display_balance())  
    print(my_account.deposit(500))     
    print(my_account.withdraw(100))    
    print(my_account.display_balance())  