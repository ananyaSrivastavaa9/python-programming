import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

print("💖 LOVE CALCULATOR 💖")

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

percentage = random.randint(50, 100)

result = f"{name1} ❤️ {name2} = {percentage}% Love"

speak(result)

if percentage > 85:
    speak("Perfect match. Made for each other.")
elif percentage > 70:
    speak("Strong love connection.")
elif percentage > 55:
    speak("Good compatibility.")
else:
    speak("Needs effort and understanding.")
