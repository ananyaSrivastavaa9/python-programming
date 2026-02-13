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

# def subtract(a,b):
#     print("difference is :",(a-b))
# subtract()

# variable-length arguments

    # *args(arbitary arguments)
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("Ms.", "Ananya", "Srivastava")

# eg 2
def add_num(*num):
    total = 0
    for number in num:
        total += number
    return total

print(add_num(1,2,3))

    # Keyword Arbitrary Arguments (**kwargs)
def greet(**wish):
    for key,value in wish.items():
        print(key, "says", value)
greet(Ananya = "Hi", Minal = "hey", Priya = "hello")

# return statement
def sum(a,b):
    sum = a+b
    return sum
print(sum(1,2))

def name(name1, name2, name3):
    return "Hello" + " " + name1 + " " + name2 + " " + name3
print(name("Ananya", "Minal", "Priya"))