import speech_recognition as sr
import pyttsx3
import pydirectinput
import pyautogui
import webbrowser
import time
import subprocess

#Allow the voice assistant to talk
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#Listen to user input
def listen():
    
    #Obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    #Recognize speech using google
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)

        #normalize the query
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from the speech recognition service. {0}".format(e))

#Function to click button until absent

def auto_story():
   
    pixel_color = (233, 233, 233)
    while (pyautogui.pixel(1678, 33) != pixel_color):
        pydirectinput.moveTo(1536, 753)
        print("AM CLICKING")
        pydirectinput.click()
        time.sleep(.05)


if __name__ == "__main__":
    time.sleep(2)
    auto_story()
    #pyautogui.displayMousePosition()
    #1536 753 coordinates for button
    #X:1678 Y:41 coordinates for backpack icon

    # speak("Hi! How can I assist you?")
    # command = listen()
   