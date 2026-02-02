# exception handling
a = input("enter a number: ")
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*int(i)}")
except:
    print("sorry")