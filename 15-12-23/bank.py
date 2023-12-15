class Bank_Account:
    def __init__(self, acc_no, name, acc_type, ):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Bank")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance ")
    def display(self):
        print("Mr." , self.name, "with", self.acc_type, "account No. " , self.acc_no)
        print("has : Net Available Balance=",self.balance)
s = Bank_Account(12345, "ABC", "Saving")
s.deposit()
s.withdraw()
s.display()
