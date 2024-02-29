print('- string are arrays') 
a = 'hello, world'
print(a[1])

print('- Looping Through a String') 
for x in 'banana':
    print(x)

print('- String Length') 
a = 'hello, world'
print(len(a))

print('- Check String') 
txt = 'the best thing in life are free!'
print('free' in txt)
if 'free' in txt:
    print("yess, 'free' is present")

print('- Check if NOT') 
txt = 'the best thing in life are free!'
print('expensive' not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

print('- Slicing') 
b = 'hello, world!'
print(b[1:5])

print('- Clice from the start')
b = 'hello world!'
print(b[:5])

print('- Clice from the end')
b = 'hello world!'
print(b[2:])

print('- negative indexing')
b = 'hello world!'
print(b[-5:-2])

print('- upper case')
b = 'hello world!'
print(a.upper())

print('- lower case')
b = 'Hello World!'
print(a.lower())

print('- remove whitespace')
b = ' Hello World!'
print(a.strip())

print('- replace string')
b = 'Hello World!'
print(b.replace('H', 'J'))

print('- split string')
b = 'Hello, World!'
print(b.split(','))

print('- string format')
quantity = 3
itemno = 567
price = 49.95
myorder = "i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "i want {2} pieces of item {1} for {0} dollars."
print(myorder.format(quantity, itemno, price))