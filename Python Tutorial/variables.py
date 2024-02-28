print('# Createng') # createing
x = 5
y = "sakti"
y = "Norma"
Y = "Norman"
print(x,y)

# casting
x = str(3) # x = '3'
y = int(3) # y = 3
z = float(3) # z = 3.0

print('# get the type') # get the type
x = 5
y = "sakti"
print(type(x))
print(type(y))

# multi words variable names
# camel case names
myVariableName = "sakti"
# Pascal case names
MyVariableName = "sakti"
# Snake case names
my_variable_name = "sakti"

print('# many valuee to multiple variables') # many values to multiple variables
x, y, z = 'orange', 'banana', 'cherry'
print(x, y, z)

print('# one valuee to multiple variables') # one values to multiple variables
x = y = z = 'orange'
print(x, y, z)

print('# unpack collection') # unpack collection
fruits = ['apple', 'orange', 'banana']
x, y, z = fruits
print(x, y, z)

print('# Output Variables') # Output Variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print('# globaal variable') # global variable
x = 'awsome'

def myfunc():
    print('python is ' + x)

myfunc()

print('# global keyword') # global keyword
def myfunc():
    global x
    x = 'fantastic'

myfunc()
print('python is ' + x)