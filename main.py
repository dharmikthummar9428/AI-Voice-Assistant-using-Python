import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia
import requests
import smtplib
from email.message import EmailMessage
import config



def wait_for_wake_word():

    speak("Say alexa to wake me.")

    while True:
        text = listen()

        if "alexa" in text:
            speak("Yes")
            return
        
# TEXT TO SPEECH 

def speak(text):
    print("Assistant:", text)
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


#SPEECH TO TEXT 

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 300
        audio = r.listen(source, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio, language="en-in")
        print("You:", command)
        return command.lower()

    except:
        return ""


#WEATHER 

def get_weather():

    url = f"http://api.openweathermap.org/data/2.5/weather?q={config.CITY}&appid={config.WEATHER_API_KEY}"

    data = requests.get(url).json()

    temp = data["main"]["temp"] - 273.15
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    weather_text = f"Temperature is {temp:.1f} degree celsius with {desc} and humidity {humidity} percent"

    return weather_text


#EMAIL

def send_email(to, subject, content):

    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = config.EMAIL
    msg["To"] = to

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(config.EMAIL, config.EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()


#SMART REPLY

def smart_reply(command):

    if "your name" in command:
        return "I am your voice assistant."

    elif "how are you" in command or "how r u" in command:
        return "I am doing well, thank you for asking! As an AI, I don't have feelings, but I am fully operational and ready to help you."

    elif "who made you" in command:
        return "I was created using Python."

    return None


#COMMAND HANDLER

def handle_command(command):

    # Open YouTube
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # Google Search
    elif "search" in command:

        query = command.replace("search", "").strip()

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        speak("Searching Google")

    # Play Song
    elif "play song" in command:
        speak("Opening yt music")
        webbrowser.open("https://music.youtube.com")

    elif "play music on youtube" in command or "play music" in command:

        speak("Which song should I play?")
        song = listen()

        speak(f"Playing {song} on YouTube")

        
        pywhatkit.playonyt(song)
    
    elif "play music on spotify" in command:

        speak("Which song should I play?")
        song = listen()

        query = song.replace(" ", "%20")

        url = f"https://open.spotify.com/search/{query}"

        webbrowser.open(url)

        speak("Opening Spotify")

    # Time
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    # Weather
    elif "weather" in command:

        speak("Checking weather")

        weather = get_weather()

        speak(weather)
        # print(data)

    # Wikipedia
    elif "who is" in command or "what is" in command:
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("Sorry I could not find information")

    #WhatsApp
    elif "send message" in command:

        speak("Please type the phone number with country code")
        number = input("Enter number (+911234567890): ").strip()

        speak("What message should I send")
        message = listen()

        import urllib.parse

        encoded_msg = urllib.parse.quote(message)

        number_clean = number.replace("+", "")

        url = f"https://wa.me/{number_clean}?text={encoded_msg}"

        webbrowser.open(url)

        speak("WhatsApp opened. Please press enter to send the message.")

    # Send Email
    elif "send email" in command:
        speak("Please type the receiver email address")
        to = input("Enter receiver email: ").strip()

        speak("Tell me subject")
        subject = listen()

        speak("What should I say")
        content = listen()

        send_email(to, subject, content)
        speak("Email sent")

    elif "stop" in command or "exit" in command:
        speak("Have a Great day , Goodbye!!")
        exit()

    else:
        # Smart reply
        reply = smart_reply(command)

        if reply:
            speak(reply)
        else:
            speak("I did not understand. Searching Google.")
            webbrowser.open(f"https://www.google.com/search?q={command}")


def main():

    while True:

        wait_for_wake_word()

        command = listen()

        if command == "":
            continue

        handle_command(command)

if __name__ == "__main__":
    main()