print('\n- Exeption Handling')
try:
    print(x)
except:
    print("An xception occured")

print('\n- Many Exceptions')
try:
    print(x)
except NameError:
    print('variable x is not defind')
except:
    print('something else went wrong')

print('\n- Else')
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print('\n- Finally')
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
    

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

print('\n- Raise an exception')
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

print('\n----')
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")