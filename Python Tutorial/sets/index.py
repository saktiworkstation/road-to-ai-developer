print('sets unordered, unchangeable*, and unindexed.')
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print('- Get the Length of a Set')
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

print('- Set Items - Data Types')
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(type(set1))

print('- The set() Constructor')
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)