print('- change tuple values')
x = ('aple', 'banana', 'cherry')
y = list(x)
y[1] =  'kiwi'
x = tuple(y)

print(x)

print('- add items')
x = ('aple', 'banana', 'cherry')
x.append('kiwi')
thistuple = tuple(x)
# .
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)