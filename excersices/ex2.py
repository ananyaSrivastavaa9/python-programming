# Index should be same
# questions[0] → answers[0] → prize[0]

questions = [
    "What is the capital of India?",
    "Which language is used for web apps?",
    "Who developed Python?",
    "What is 2 + 2?",
]

answers = [
    "delhi",
    "python",
    "guido van rossum",
    "4"
]

prize = [1000, 2000, 5000, 10000]

money = 0

for i in range(len(questions)):
    print("\nQuestion for ₹", prize[i])
    print(questions[i])
    
    user_ans = input("Your answer: ").lower()

    if user_ans == answers[i]:
        money = prize[i]
        print("✅ Correct answer!")
        print("You have won ₹", money)
    else:
        print("❌ Wrong answer!")
        print("You take home ₹", money)
        break