# exception handling

# a = input("enter a number: ")
# print(f"multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {int(i)} = {int(a)*int(i)}")
# except:
#     print("sorry ")

try:
    num = int(input("enter a num: "))
except:
    print("no entered is not interger")