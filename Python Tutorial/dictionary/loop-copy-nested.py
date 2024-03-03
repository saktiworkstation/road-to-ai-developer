print('- loop through a dictinary')
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

print('- all values')
for x in thisdict:
    print(thisdict[x])

print('- use the values()')
for x in thisdict.values():
    print(x)

print('- use the keys()')
for x in thisdict.keys():
    print(x)

print('- keys and values, by using the items()')
for x, y in thisdict.items():
    print(x, y)

print('- copy a dictionary')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print('- Make a copy of a dictionary with the dict() function')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

print('- Create a dictionary that contain three dictionaries')
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

print('- Create three dictionaries, then create one dictionary that will contain the other three dictionaries')

child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

print('- Access Items in Nested Dictionaries')
print(myfamily["child2"]["name"])