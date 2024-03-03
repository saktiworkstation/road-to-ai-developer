print('- demo')
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': '1964'
}
print(thisdict)

print('- Dictionary Items')
thisdict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1965
}
print(thisdict['brand'])

print('- Duplicates Not Allowed')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

print('- length')
print(len(thisdict))

print('- Dictionary Items - Data Types')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

print('- The dict() Constructor')
thisdict = dict(name = 'sakti', age = 19, country = 'indonesia')
print(thisdict)