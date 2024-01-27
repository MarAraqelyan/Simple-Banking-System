import accounts
import customers


c1 = customers.Customer("Ilon Mask", 00000000)

a1 = accounts.IndividualAccount(c1, "USD", "checking", 1256821566)
a2 = accounts.IndividualAccount(c1, "USD", "checking", 7845652645)

a2.deposit(5000)

a2.transfer(a1, 4000)

a1.withdraw(2000)

print(a1.get_balance())
print(a2.get_balance())

print(a1.view_history())
print(a2.view_history())