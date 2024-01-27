from customers import Customer
from abc import ABC, abstractmethod
import transactions
from customExceptions import NotEnoughBalanceError

class ValidAmount:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name 

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Must be a number")
        if value < 0:
            raise ValueError("Must be non-negative")
        instance.__dict__[self.property_name] = value



class ValidAccountNumber:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name 

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Must be a number")
        if len(str(value)) < 8:
            raise ValueError("Must have 8 characters")
        instance.__dict__[self.property_name] = value




class IAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        ...

    @abstractmethod
    def withdraw(self, amount):
        ...

    @abstractmethod
    def transfer(self, tr_account, amount):
        ...
    
    
    

    
    

class IndividualAccount(IAccount):
    amount = ValidAmount()
    account_number = ValidAccountNumber()

    def __init__(self, customer, currency, type, account_number):
        self._balance = 0
        self.account_number = account_number
        self._customer = customer
        self._currency = currency
        self._type = type
        self.history = {}

    
    def deposit(self, amount):
        self.amount = amount
        transaction = transactions.DepositTranscation(self.amount, self.account_number, self._currency)
        self._balance += self.amount
        transaction.save_history(self.history)


    def withdraw(self, amount):
        self.amount = amount
        transaction = transactions.WithdrawTransaction(self.amount, self.account_number, self._currency)
        if self.amount > self._balance:
            raise NotEnoughBalanceError
        self._balance -= self.amount
        transaction.save_history(self.history)

    def transfer(self, tr_account, amount):
        if amount > self._balance:
            raise NotEnoughBalanceError
        self._balance -= amount
        tr_account._balance += amount


    def get_balance(self):
        return self._balance
    
    def view_history(self):
        return self.history
        


class JointAccount(IAccount):
    amount = ValidAmount()
    account_number = ValidAccountNumber()

    def __init__(self, *customers, currency, type, account_number):
        self._balance = 0
        self.account_number = account_number
        self._customers = customers 
        self._currency = currency
        self._type = type
        self.history = {}


    def deposit(self, amount):
        self.amount = amount
        transaction = transactions.DepositTranscation(self.amount, self.account_number, self._currency)
        self._balance += self.amount
        transaction.save_history(self.history)


    def withdraw(self, amount):
        self.amount = amount
        transaction = transactions.WithdrawTransaction(self.amount, self.account_number, self._currency)
        if self.amount > self._balance:
            raise NotEnoughBalanceError
        self._balance -= self.amount
        transaction.save_history(self.history)


    def transfer(self, tr_account, amount):
        if amount > self._balance:
            raise NotEnoughBalanceError
        self._balance -= amount
        tr_account._balance += amount


    def get_balance(self):
        return self._balance
    
    def view_history(self):
        return self.history
