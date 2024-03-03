print('- condition if')
a = 33
b = 200
if b > a:
    print('b is greater')

print('- condition elif')
a = 34
b = 34
if b > a:
    print('b is greater')
elif b == a:
    print('a and b are equal')

print('- condition else')
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print('- Short Hand If')
if a > b: print('a is greater than b')

print('- Short Hand If')
a = 2
b = 330
print("A") if a > b else print('B')
print("A") if a > b else print("=") if a == b else print("B")

print('- And on if')
a = 200
b = 33
c = 500
if a > b and c > a:
    print('both condition are True')

print('- Or on if')
a = 200
b = 33
c = 500
if a > b or a > c:
    print('at least one of the condition is True')

print('- Not on if')
a = 33
b = 200
if not a > b:
    print('a is NOT greater than b')

print('- Nested If')
x = 41
if X > 10:
    print('above ten, ')
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20.')

print('- The pass Statement')
a = 33
b = 200

if b > a:
    pass