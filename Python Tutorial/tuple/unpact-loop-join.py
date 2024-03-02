print('- unpact tuples')
fruits = ['aple', 'banan', 'chery']

(green, yellow, red) = fruits

print(green, yellow, red)

print('- using asterisk')
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green, yellow, red)

(green, yellow, *red) = fruits
print(green, yellow, red)

print('- looping')
thistuple = ('apple', 'banana', 'cherry', 'straw')
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

print('- Join Two Tuples')
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print('- Multiply Tuples')
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)