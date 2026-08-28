#  create a python program using class,object,inheritance,constructor and user input . create a base class BankAccount with Account no,holder name,and balance . create a derived class SavingAccount with interest rate . Take input input from user and calculate the interest and final balance
class BankAccount:
  def __init__(self,no,name,balance):
    self.no = no
    self.name = name
    self.balance = balance
  def display(self):
    print("Account Number : ",self.no)
    print("Account Holder Name : ",self.name)
    print("Bank Balance : ",self.balance)
class SavingAccount(BankAccount):
  def __init__(self, no, name, balance,interest_rate):
    super().__init__(no, name, balance)
    self.interest_rate = interest_rate
  def calculate (self):
    interest = self.balance*self.interest_rate/100
    Total_balance = interest+self.balance
    super().display()
    print("Interest Rate : ",self.interest_rate)
    print("Interest : ",interest)
    print("Total Balance : ",Total_balance)
no = input("enter your account number : ")
name = input("Enter Account holder name : ")
balance = int(input("Enter current balance : "))
interest_rate= int(input("Enter interest rate : "))
obj = SavingAccount(no,name,balance,interest_rate)
obj.calculate()    