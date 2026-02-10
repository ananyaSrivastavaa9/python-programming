def avg(a,b):
    print("average is :", (a+b)/2)
avg(5,6)

# default arguments
def sum(a=2,b=1):
    print("Sum is :",(a+b))
sum(1) # a = 1 (changed from default)
sum(b=2) # b = 2 (changed from default)

# keyword arguments
def name(name, age, section):
    print("hello", name, age, section)
name(age = 18, section = "B", name = "Ananya") #order does not matter

#required arguments
def subtract(a,b):
    print("difference is :",(a-b))
subtract()

