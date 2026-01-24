import time

hour = time.localtime().tm_hour

if hour >= 5 and hour <= 11 :
    print("Good Morning!")
elif hour >= 12 and hour <= 17 :
    print("Good Afternoon!")
elif hour >= 18 and hour <= 21 :
    print("Good Evening!")
else :
    print("Good Night!")