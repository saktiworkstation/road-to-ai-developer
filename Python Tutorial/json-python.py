print('\n- json in python')
import json
x = '{"name": "Sakti", "age": 19, "city": "Karanganyar"}'

y = json.loads(x)
print(y['age'])

print('\n- convert from python to json')
x = {
    "name": "Sakti",
    "age": 19,
    "city": "Karanganyar"
}
y = json.dumps(x)
print(y)

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))
print('\n- Format the Result')
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print('\n order the result')
print(x, indent=4, sort_keys=True)