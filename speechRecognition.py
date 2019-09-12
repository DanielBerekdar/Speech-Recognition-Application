import speech_recognition as sr
import pyttsx3 as tts
import re

# TODO: Based on the number parsed from the String literal, find out which chapters are due for that week
def findChapter(week):
    if week == 0:
        output("Chapter 1")
        print("Chapter 1")
    elif week == 1:
        output("Chapters 2 to 3")
        print("Chapters 2 to 3")
    elif week == 3:
        output("Chapters 4 to 6")
        print("Chapters 4 to 6")
    elif week == 4:
        output("Congratulations, there is no class on this week!")
        print("Congratulations, there is no class on this week!")
    elif week == 5:
        output("Chapters 7 to 8")
        print("Chapters 7 to 8")
    elif week == 6:
        output("Chapters 9 to 10")
        print("Chapters 9 to 10")
    elif week == 7:
        output("Chapters 11 to 12")
        print("Chapters 11 to 12")
    elif week == 8:
        output("Chapters 13 to 14")
        print("Chapters 13 to 14")
    elif week == 9:
        output("Chapters 15 to 16")
        print("Chapters 15 to 16")
    elif week == 10:
        output("Congratulations, there is no class on this week!")
        print("Congratulations, there is no class on this week!")
    elif week == 11:
        output("Chapters 17 to 18")
        print("Chapters 17 to 18")
    elif week == 12:
        output("Chapters 19 to 20")
        print("Chapters 19 to 20")
    elif week == 13:
        output("Chapters 21 to 22")
        print("Chapters 21 to 22")
    elif week == 14:
        output("Chapters 23 to 25")
        print("Chapters 23 to 25")
    elif week == 15:
        output("Student Presentations, good luck!")
        print("Student Presentations, good luck!")
    else:
        output("You have entered an invalid week.")
        print("You have entered an invalid week.")


# TODO: This function will take in a String literal and output it using TTS:
def output(msg):
    engine = tts.init()
    engine.setProperty('rate', 150)
    engine.say('{}'.format(msg))
    engine.runAndWait()


# TODO: Using the  microphone as a source for the speech recognition module to read the voice as input and store it as a String literal:
recognizer = sr.Recognizer
with sr.Microphone() as source:
    print("Speak!")
    audioInput = recognizer().listen(source)
    try:
        voiceToText = recognizer().recognize_google(audioInput)
        print("Your input was: " + voiceToText)
        sentence = voiceToText
        result = map(int, re.findall('\d+', sentence))
        for res in result:
            weekNum = res
    except sr.UnknownValueError:
        print("There was an issue recording your microphone input.")
        output("There was an issue recording your microphone input.")

try:
    findChapter(weekNum)
except:
    output("A day of the week was unable to be processed by your Input.")
    print("A day of the week was unable to be processed by your Input.")
