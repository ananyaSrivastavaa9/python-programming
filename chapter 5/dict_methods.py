# update()
a = {1:65,2:68,3:99,4:87}
b = {5:87,6:99}
a.update(b)
print(a)

info = {'name' : 'Ananya', 'age' : 18, 'eligible' : True}
print(info)
info.update({'age': 19})
print(info)

# clear()
a.clear()
print(a)

# pop()
a.pop(1)
print(a)

# popitem()
a.popitem()
print(a)

# del:
del a
print(a)