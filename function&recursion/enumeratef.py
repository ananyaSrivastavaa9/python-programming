marks = [2, 89, 56, 34, 74, 98, 32]
for index, mark in enumerate(marks):
        print(index, mark)
        if (index == 5):
            print("Ananya")

''' 0 2
    1 89
    2 56
    3 34
    4 74
    5 98
    Ananya
    6 32 ''' 


for index, mark in enumerate(marks, start = 1):
        print(index, mark)
        if (index == 5):
            print("Ananya")

''' 1 2
    2 89
    3 56
    4 34
    5 74
    Ananya
    6 98
    7 32 '''