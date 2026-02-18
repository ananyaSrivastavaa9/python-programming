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