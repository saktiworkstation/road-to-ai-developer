print('- demo class')
class Test:
    x = 99

print(Test.x)

print('- create Object')
class Test:
    x = 99
p1 = Test()
print(p1.x)

print('- The __init__() Function')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Sakti", 19)
print(p1.name)
print(p1.age)

print('- The __str__() Function')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Sakti", 19)
print(p1)

print('- Object Methods')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)
    
p1 = Person("Sakti", 19)
p1.myfunc()

print('- The self Parameter')
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Sakti", 19)
p1.myfunc()

print('- Modify Object Properties')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Sakti", 19)
p1.age = 20
print(p1.age)

print('- Delete Object Properties')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Sakti", 19)
del p1.age
print(p1.age)

print('- Delete Object Properties')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Sakti", 19)
del p1
print(p1)
