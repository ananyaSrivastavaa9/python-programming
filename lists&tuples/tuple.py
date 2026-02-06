tup = (1,2,3,4)
print(type(tup),tup)

# if storing one variable
a = (1,)
print(type(a),a)

# indexing of tuple
print(tup[0])
print(tup[1])

# negative indexing
print(tup[-2])
print(tup[len(tup)-2])
print(tup[4-2])
# print(tup[2])

# checking for an item
if 5 in tup:
    print("yes")

# range
print(tup[0:3:2])