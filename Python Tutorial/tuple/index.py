print('- basic tuple')
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('- tuple length')
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print('- Create Tuple With One Item')
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print('- Tuple Items - Data Types')
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")

print('- The tuple() Constructor')
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)