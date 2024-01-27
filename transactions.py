from abc import ABC, abstractmethod
from customExceptions import NotEnoughBalanceError

         

class Transaction(ABC):
    @abstractmethod
    def save_history(self, trans):
        ...


class DepositTranscation(Transaction):
    def __init__(self, amount, account_number, currency):
        self._amount = amount
        self._account_number = account_number
        self.currency = currency

    def save_history(self, history):
        history["deposit"] = (self._account_number, self._amount, self.currency)
    

class WithdrawTransaction(Transaction):
    def __init__(self, amount, account_number, currency):
        self._amount = amount
        self._account_number = account_number
        self.currency = currency

    def save_history(self, history):
        history["withdraw"] = (self._account_number, self._amount, self.currency)




            

        

