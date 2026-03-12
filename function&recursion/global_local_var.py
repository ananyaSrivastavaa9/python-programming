# local Variable
def my_function():
    x = 5
    print(x)
my_function()

# Global Variable
def my_function():
    global x #used a global keyword
    x = 5
my_function()
print(x)

# global 2
x = 5 
def my_function():
    print(x)
my_function()