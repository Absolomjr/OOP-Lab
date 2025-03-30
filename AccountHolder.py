class AccountHolder:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_account_info(self):
        return f"Account Holder: {self.name}, Age: {self.age}, Address: {self.address}"

class LoanAccount(AccountHolder):
    def __init__(self, name, age, address, loan_amount=0, interest_rate=0.05):
        super().__init__(name, age, address)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
    
    def apply_for_loan(self, amount):
        self.loan_amount += amount
        print(f"{self.name} has been approved for a loan of {amount}.")
    
    def repay_loan(self, amount):
        if amount > self.loan_amount:
            print(f"Error: Repayment amount exceeds loan balance of {self.loan_amount}.")
        else:
            self.loan_amount -= amount
            print(f"{self.name} has repaid {amount}. Remaining balance: {self.loan_amount}.")
    
    def display_loan_info(self):
        account_info = self.display_account_info()
        return f"{account_info}, Loan Balance: {self.loan_amount}, Interest Rate: {self.interest_rate*100}%"

# Creating two LoanAccount objects
loan1 = LoanAccount("Alice Johnson", 30, "123 Elm St")
loan2 = LoanAccount("Bob Smith", 40, "456 Oak St")

# Applying for loans
loan1.apply_for_loan(5000)
loan2.apply_for_loan(10000)

# Repaying loans
loan1.repay_loan(2000)
loan2.repay_loan(12000)  # This should trigger an error

# Displaying loan details
print(loan1.display_loan_info())
print(loan2.display_loan_info())
