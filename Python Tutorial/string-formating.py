print('\n string formatting')
price = 49
txt = 'the price is {} dollars'
print(txt.format(price))

print('\n Multiple Values')
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.3f} dollars."
print(myorder.format(quantity, itemno, price))

print('\n Index Numbers')
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.3f} dollars."
print(myorder.format(quantity, itemno, price))

print('\n Index Numbers')
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))