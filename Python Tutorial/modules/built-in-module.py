import platform

from mymodule import person1

x = platform.system()
print(x)

x = dir(platform)
print(x)

print(person1['age'])