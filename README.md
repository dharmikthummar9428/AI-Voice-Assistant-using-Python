# AI-Voice-Assistant-using-Python


# Project Description:
This project is a Python-based AI Voice Assistant capable of recognizing voice commands and performing various tasks such as opening websites, searching information on Google, playing music, checking weather updates, sending WhatsApp messages, and sending emails.
The assistant uses speech recognition to understand user commands and text-to-speech technology to respond. It integrates several APIs and Python libraries to automate common tasks and provide a simple voice-controlled interface.


# Features:
Voice command recognition,
Text-to-speech responses,
Google search through voice commands,
Play music on YouTube and Spotify,
Open websites like YouTube,
Get current weather information,
Wikipedia information retrieval,
Send WhatsApp messages,
Send emails using SMTP,
Smart conversational replies,
The system continuously listens for a wake word ("Alexa") before processing commands.


# Technologies Used:
Python,
SpeechRecognition,
Pyttsx3,
Requests,
Wikipedia API,
OpenWeather API,
SMTP Email Protocol,
PyWhatKit


# Working:
The assistant waits for the wake word "Alexa".
After activation, it listens for user commands.
Speech is converted to text using the SpeechRecognition library.
The command is processed and appropriate actions are performed.
Responses are spoken using the text-to-speech engine.
