# handling custom error
class AgeError(Exception):
    pass
try:
    age = -2
    if age < 0:
        raise AgeError("Age Could not be negative")
except AgeError as e:
    print(e)