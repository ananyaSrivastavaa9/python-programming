print("enter first number")
a = int(input())
print("enter second number")
b = int(input())
print("enter 1 for addition")
print("enter 2 for substraction")
print("enter 3 for multiply")
print("enter 4 for division")
operations = int(input())
if operations == 1:
    print("the value of", a, "+", b, "=", a + b)
    
elif operations == 2:
    print("the value of", a, "-", b, "=", a - b)
        
elif operations == 3:
    print("the value of", a, "*", b, "=", a * b)
            
elif operations == 4:
    print("the value of", a, "/", b, "=", a / b)