print('- demo')
fruits = ['apple', 'orange', 'banana', 'cherry']
for x in fruits:
    print(x)

print('- Looping Through a String')
for x in "banana":
    print(x)

print('- The break Statement')
fruits = ['apple', 'orange', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print('- The continue Statement')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('- The range() Function')
for x in range(6):
    print(x)

for x in range(3, 9):
    print(x)

for x in range(2, 30, 3):
    print(x)

print('- Else in For Loop')
for x in range(6):
    print(x)
else:
    print("Finally finished")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

print("- Nested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("- The pass Statement")
for x in [0, 1, 2]:
    pass