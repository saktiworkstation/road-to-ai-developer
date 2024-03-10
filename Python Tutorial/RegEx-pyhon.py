print('\nDemonstration')
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print('Yes We have a match')
else:
    print('No match')

print('\n- the findall() function')
txt = 'the rain in Spain'
x = re.findall('ai', txt)
print(x)
x = re.findall("Portugal", txt)
print(x)

print('\n- The search() Function')

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print('\n- The search() Function')
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

print('\n- The sub() Function')
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

print('\n- Match Object')
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())