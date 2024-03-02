print('- join two sets')
set1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('- join')
set3 = set1.union(set2)
print(set3)
print('- update')
set1.update(set2)
print(set1)
# * Both union() and update() will exclude any duplicate items.

print('- Keep ONLY the Duplicates')
print('- intersection_update')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
print('- intersection')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

print('- Keep All, But NOT the Duplicates')
print('- symmetric_difference_update')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
print('- symmetric_difference')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)