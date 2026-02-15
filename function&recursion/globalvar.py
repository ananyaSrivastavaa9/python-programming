# global variable works outside the function also
subject = "Python"
def study():
    print(subject)
study()
print(subject)