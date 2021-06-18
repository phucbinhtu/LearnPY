import speech_recognition
import pyttsx3
from datetime import date, datetime

def xuly(dauvao):
    if dauvao=="":
        robot="I can't hear you, try again ."
    elif dauvao=='hello':
        robot='Hello Phuc'
    elif "today" in dauvao:
        today=date.today()
        robot=today.strftime("%B %d, %Y")
    elif "time" in dauvao:
        now=datetime.now()
        robot=now.strftime("%H hours %M minutes %S seconds")
    elif "president" in dauvao:
        robot="Joe Biden"
    else:
        robot="I'm fine thank you, and you ?"
    return robot

robot_ear=speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening ...")
        audio=robot_ear.listen(mic)
    print("Robot:...")
    try:
        you=robot_ear.recognize_google(audio)
    except:
        you=""
    print("You: " + you)
    #Phan hieu
    robot_brain=xuly(you)
    print("Robot: "+robot_brain)
    #Phần nói
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    if "bye" in you:
        break
