import datetime

print('\n- dates')
x = datetime.datetime.now()
print(x)

print('\n- date output')
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

print('\n- creating data object')
x = datetime.datetime(2024, 3, 8)
print(x)

print('\n- the strTime() method ')
x = datetime.datetime(2024, 3, 8)
print(x.strftime("%B"))