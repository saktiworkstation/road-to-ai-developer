print('- List Items')
thislist = ['aple', 'banana', 'cherry', 'aple']
print(thislist)

print('- List Length')
thislist = ['aple', 'banana', 'cherry']
print(len(thislist))

print('- List Items - Data Types')
list1 = ['aple', 'banana', 'cherry']
list2 = [1,2,3]
list3 = [True, False, False, True]
list4 = ["abc", 34, True, 40, "male"]
thislist = list(("apple", "banana", "cherry"))

print(type(list1))
print(thislist)

print('- Access Items')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

print('- Check Items Exist')
if "apple" in thislist:
    print('Yes, Apple is in thislist')

print('- Change Item Value')
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print('- Insert Items')
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print('- Append  Items')
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print('- Extend List')
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print('- Add Any Iterable')
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print('- Remove Specified Item')
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print('- Remove Specified Index')
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print('- Clear the List')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)