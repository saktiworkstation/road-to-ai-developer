print('- demo and access items')
cars = ['ford', 'mclaren', 'bmw']
x = cars[1]
print(x)
cars[0] = 'Toyota'
x = cars[0]
print(x)

print('- The Length of an Array')
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

print('- The Length of an Array')
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

print('- The Length of an Array')
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

print('- Removing Array Elements')
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)