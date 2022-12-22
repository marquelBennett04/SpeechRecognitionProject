import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

while True:

    try:

        with sr.Microphone() as mic:

            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)

            text = r.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

    except sr.UnknownValueError():

        recognizer = sr.Recognizer()
        continue
