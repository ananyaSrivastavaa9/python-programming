questions = [
    "What is the capital of India?",
    "Who is known as the Father of the Nation in India?",
    "Which planet is known as the Red Planet?",
    "What is the national animal of India?",
    "How many days are there in a leap year?",
    "Which gas do plants absorb from the atmosphere?",
    "Who invented the computer?",
    "Which is the largest ocean in the world?",
    "What is the square root of 64?",
    "Which language is used to write Python programs?"
]
answers = [
    "new Delhi",
    "mahatma Gandhi",
    "mars",
    "tiger",
    "366",
    "Carbon Dioxide",
    "Charles Babbage",
    "Pacific Ocean",
    "8",
    "Python"
]
price = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money = 0
for i in range(len(questions)):
    print("Question for Rs.", price[i])
    print(questions[i])
    user_ans = input("Enter your answer: ")

    if user_ans == answers[i]:
        print("You Won Rs", price[i])
    else:
        print("Go Home")
        break