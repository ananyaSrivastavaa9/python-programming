#cube
f = lambda a : a*a*a
result = f(2)
print(result)

# sum
f = lambda a,b : a+b
result = f(5,3)
print(result)

# filter()
def is_even(a):
    return a%2==0
nums = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(is_even,nums))
print(result)