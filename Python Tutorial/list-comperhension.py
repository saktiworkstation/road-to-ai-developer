print('- List Comprehension')
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print('- Condition')
newlist = [x for x in fruits if x != "apple"]

print('- Condition')
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]

print('- Expression')

newlist = [x.upper() for x in fruits]