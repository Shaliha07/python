class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"${amount} deposited. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds."
        else:
            self.__balance -= amount
            return f"${amount} withdrawn. New balance: ${self.__balance}"

    def get_balance(self):
        return f"Balance for {self.owner}: ${self.__balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._BankAccount__balance * self.interest_rate
        self.deposit(interest)
        return f"Interest applied: ${interest}. New balance: ${self._BankAccount__balance}"

# Create a savings account and apply interest
savings_account = SavingsAccount("Shaliha", 1000)
print(savings_account.apply_interest())
print(savings_account.get_balance())
