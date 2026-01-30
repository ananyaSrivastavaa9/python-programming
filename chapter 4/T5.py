# Write a program to sum a list with 4 numbers.
a = []
total = 0
for i in range(4):
    num = int(input("enter numbers: "))
    total = total+num
    a.append(num)
print(a)
print(total)