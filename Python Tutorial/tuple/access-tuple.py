print('- acess tuple items')
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print('- negative indexing')
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print('- range of indexes')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

print('- Check if Item Exists')
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")