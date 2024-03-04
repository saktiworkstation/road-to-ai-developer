print('- demo')
i = 1
while i < 6:
    print(i)
    i += 1

print('- break statement')
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print('- else statement')
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')