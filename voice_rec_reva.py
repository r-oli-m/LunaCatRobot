import speech_recognition as sr
import datetime 
from gpiozero import LED
import time
import sched, time
import pygame
import random
import pyttsx3

start1 = time.time()
start = time.time()
wTimeStarted = False
bTimeStarted = False
wTimeFinished = False
bTimeFinished = False


r = sr.Recognizer()
mic = sr.Microphone()

print("hello")
pygame.mixer.init()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')
engine.setProperty('rate', 120)
engine.say("Hi I'm Luna!")
engine.runAndWait()

# s = sched.scheduler(time.time, time.sleep)
# def do_smthg(sc):
#     print("doing stuff...")
#     sc.enter(60, 1, do_smthg, (sc,))
#     
# s.enter(60, 1, do_smthg, (s,))
# s.run()

def songPicker():
    songsList = ["zero.wav", "one.wav", "two.wav", "three.wav",
                 "four.wav", "five.wav", "six.wav", "seven.wav",
                 "eight.wav", "nine.wav", "ten.wav", "eleven.wav"
                 "twelve", "thirteen"]
    numPicked = random.randint(0, 13)
    print(songsList[numPicked])
    return songsList[numPicked]

def meowPicker():
    meowList = ["meow0.wav", "meow1.wav", "meow2.wav", "meow3.wav", "meow4.wav"]
    numPicked = random.randint(0, 4)
    print(meowList[numPicked])
    return meowList[numPicked]
    

while True:
    
    with mic as source:
        print("i'm before listen")
        audio = r.listen(source)
        print("i'm here before google")
        try:
            words = r.recognize_google(audio).lower()
        except:
            continue
        print("i just finished google")
        print(f"from mic: {words}")
    print(f"from loop: {words}")
#     if(time.time() >= start + (1*60) and wTimeFinished == False and wTimeStarted == True):         # set timer 45 min
#         print("45 min end")
#         wTimeFinished = True
#         pygame.mixer.music.load("15min.wav")
#         pygame.mixer.music.play()
#         print("15 min start")
#         bTimeStarted = True
#         start1 = time.time()
#         # set timer 15 min
#     if(time.time() >= start1 + (0.5*60) and bTimeFinished == False and bTimeStarted == True):         # set timer 45 min
#         #study session end
#         print("15 min end")
#     

    if words == "today's date":
        date = datetime.datetime.now()
        date = date.strftime("%A %d %b %Y")
        print(date)
        engine.say(date)
        engine.runAndWait()
        #COME BACK
        
    if words == "play any song":
        print("yo im in")
        songPick = songPicker()
        pygame.mixer.music.load(songPick)
        pygame.mixer.music.play()

        
    if words == "stop music":
        pygame.mixer.music.stop()
        
    if words == "pause music":
        pygame.mixer.music.pause()
        
    if words == "unpause music":
        pygame.mixer.music.unpause()
    
    if words == "replay song":
        pygame.mixer.music.play()
        
    if words == "play skeletons":
        pygame.mixer.music.load("two.wav")
        pygame.mixer.music.play()
        
    if words.startswith("play song "):
        words = words.replace("play song ", "")
        
        if words == "2":
            words = "two"
        if words == "3":
            words = "three"
        if words == "for":
            words = "four"
        if words == "fix" or words == "specs" or words == "sex":
            words = "six"
        if words == "9":
            words = "nine"
        if words == "10":
            words = "ten"
        if words == "11":
            words = "eleven"
        if words == "12":
            words = "twelve"  
        if words == "13":
            words = "thirteen"
            
        try:
            songReq = words + ".wav"
            pygame.mixer.music.load(songReq)
            pygame.mixer.music.play()
        
        except:
             print("invalid command: ", songReq)
             songReq = songReq.replace(".wav", "")
             engine.say("I don't know the " + songReq + " song lol.")
             engine.runAndWait()
             continue
        
        
        
    if words == "volume lower":
        newVol = pygame.mixer.music.get_volume() - 0.35
        pygame.mixer.music.set_volume(newVol)
        
    if words == "volume higher":
        newVol = pygame.mixer.music.get_volume() + 0.35
        pygame.mixer.music.set_volume(newVol)

    if words == "start study session":
        # timer 45 min, "15 mi break" speakers --> 15 min break
        print("45 min start")
        # 45 min work time audio
        pygame.mixer.music.load("45min.wav")
        pygame.mixer.music.play()
        wTimeStarted  = True
        start = time.time()
    
    

#     if words.startswith("start timer for "): # eg 1 minute
#         words = words.replace("start timer for ", "")
#         if words == " 1 minute"
#         
#         

    if (words == "meow" or words == "talk" or words == "say something"):
        meowOut = meowPicker()
        pygame.mixer.music.load(meowOut)
        pygame.mixer.music.play()
        
    if words == "quiet" or words == "shut up" or words == "shush":
        pygame.mixer.music.stop()
        engine.stop()

    if words == "exit":
        print("...")
        engine.say("Goodbye")
        engine.runAndWait()
        break
    
    if words == "arms up":
        print("arms up")
        
