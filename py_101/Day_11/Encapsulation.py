'''
Encapsulation in Python is the concept of bundling data and the methods that operate on that data within a single unit, called a class.
It allows us to hide the internal details and implementation of an object and provide a clean and controlled interface for interacting with it.
Encapsulation hides the internal details of an object and provides methods to access and modify its state.

Let's take example of BackAccount
'''

class BankAcount:
    def __init__(self, user, account_number, balance):
        self.__user = user
        self.__account_number = account_number
        self.__balance = balance
    
    def get_account(self):
        user_account = {
            "user": self.__user,
            "account": self.__account_number
        }
        return user_account
    
    def get_balace(self):
        user_balance = {
            "account": self.__account_number,
            "balance": self.__balance
        }
        return user_balance

    def credit_balance(self, deposit_amount):
        current_balance = self.__balance 
        self.__balance = current_balance + deposit_amount
        print(f"Ammount deposited to account {self.__account_number} current balance is {self.__balance}")
        
    



        