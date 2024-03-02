print('- add items')
thisset = {'aple', 'banan', 'chery'}

thisset.add('arange')
print(thisset)

print('- add sets')
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

print('- Add Any Iterable')
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print('- Remove Item')
# ! If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
print('- discard')
# * If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
print('- pop')
# ? Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
print('- clear')
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print('- del')
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)