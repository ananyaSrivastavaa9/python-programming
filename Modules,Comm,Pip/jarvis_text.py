import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am Jarvis. Type your command.")

while True:
    cmd = input("You: ").lower()

    if "hello" in cmd:
        speak("Hello! How can I help you?")

    elif "time" in cmd:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "your name" in cmd:
        speak("My name is Jarvis.")

    elif "stop" in cmd or "exit" in cmd:
        speak("Goodbye")
        break
