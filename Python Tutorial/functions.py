print('- demonstrates')
def my_function():
    print('hello feom function')

my_function()

print('- Arguments')
def my_function(fname):
    print(fname + ' Reference')

my_function("Sakti")
my_function("Desinta")
my_function("Oreo")

print('- Number of Arguments')
def my_function(fname, lname):
    print(fname + '.' + lname )

my_function("Sakti", "Desinta")

print('- Arbitrary Arguments, *args')
def my_function(*kids):
    print('The youngest child is ' + kids[2])

my_function("Mia", "Oreo", "Miu")

print('- Keyword Arguments')
def my_function(child1, child2, child3):
    print('the youngest child is ' + child2)

my_function(child1 = 'Mia', child2 = 'Oreo', child3 = 'Miu')

print('- Arbitrary Keyword Arguments, **kwargs')

def my_function(**kid):
    print('his second name is ' + kid['sname'])

my_function(fname = 'sakti', sname = 'Desinta')

print('- Default Parameter Value')
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print('- Passing a List as an Argument')
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print('- Return Values')
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print('- The pass Statement')
def myfunction():
    pass

print('- Positional-Only Arguments')
def my_function(x, /):
    print(x)
my_function(3)

def my_function(x):
    print(x)
my_function(x = 3)

print('- Keyword-Only Arguments')
def my_function(*, x):
    print(x)
my_function(x = 3)

def my_function(x):
    print(x)
my_function(3)

print('- Combine Positional-Only and Keyword-Only')
def my_function(a, b, /, *, c, d):
    print(a, b, c, d)

my_function(5, 6, c = 7, d = 8)

print('- Recursion')
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k -1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion example Results")
tri_recursion(6)