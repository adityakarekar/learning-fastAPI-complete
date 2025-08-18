def add(num1:int,num2:int):
    return num1 + num2


def subtract(num1:int,num2:int):
    return num1 - num2

def multiply(num1:int,num2:int):
    return num1 * num2


def divide(num1:int,num2:int):
    if num2 == 0:
        return None
    return num1 / num2



class InsufficentFunds(Exception):
    pass

class BankAccount:
    
    def __init__(self,initial_balance=0):
        self.balance=initial_balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if amount> self.balance:
            raise InsufficentFunds("Insufficient funds")
        self.balance-=amount
        return self.balance

    def get_balance(self):
        return self.balance
    
    def collect_interest(self):
        self.balance=self.balance * 1.1