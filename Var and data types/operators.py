# arithmetic op
a = 1
b = 2
c = a + b
print(c)

# assignment op
a = 4-2
print(a)
b = 6
b += 3
print (b)

# comparison op
d = 6!=5
print(d)

# logical op
e = True or False
print("True or False is", True or False)
print("True or True is", True or True)
print("False or True is", False or True)
print("False or False is", False or False)

print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print(not(True))

# bitwise op
a = 5   # 0101 in binary
b = 3   # 0011 in binary
print(a & b)  # 1  (0101 & 0011 = 0001)
print(a | b)  # 7  (0101 | 0011 = 0111)
print(a ^ b)  # 6  (0101 ^ 0011 = 0110)
print(a << 1) # 10 (0101 << 1 = 1010)
print(a >> 1) # 2  (0101 >> 1 = 0010)

# identity operators
# Identity operators are used to check whether two objects are the same in memory.
a = [1,2,3,4]
b = a
c = [1,2,3,4]
print(a is b)
print(a is not c)

# membership operators
# Membership operators are used to check whether a value exists in a sequence
a = [1,2,3,4,5]
if 5 in a:
    print("yes")