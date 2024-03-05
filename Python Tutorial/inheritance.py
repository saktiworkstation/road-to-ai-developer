print('- Full example inheritance')
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print('Welcome here ', self.fname, self.lname, 'to the class of', self.graduationyear)

x = Student("Sakti", "Desinta", 2021)
x.welcome()