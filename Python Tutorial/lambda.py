print('\n- demonstrate')
x = lambda a: a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 5))

x = lambda a, b, c : a + b + c
print(x(5, 5, 5))

print('\n- why use lambda functions?')
def myfunc(n):
    return lambda a : a * n

mydouber = myfunc(2)
mydouber = myfunc(3)
print(mydouber(5))
print(mydouber(5))