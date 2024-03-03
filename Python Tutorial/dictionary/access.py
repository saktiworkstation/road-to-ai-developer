print('- accesing items')
thisdict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2024
}
x = thisdict['model']
print(x)
x = thisdict.get('model')
print(x)

print('- Get Keys')
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2020
}
x = car.keys()
print(x)

car['color'] = 'white'
print(x)

print('- Get Values')
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2020
}
x = car.values()
print(x)

car['year'] = 2024
print(x)

print('- Get Items')
car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2020
}
x = car.items()
print(x)

car['year'] = 2030
print(x)

car["color"] = "red"
print(x)

print('- Check if Key Exists')
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")