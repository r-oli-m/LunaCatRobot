import speech_recognition as sr
from datetime import date
from gpiozero import LED
import time 
import pygame
import random

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

def songPicker():
    songsList = ["zero.wav", "one.wav", "two.wav", "three.wav",
                 "four.wav", "five.wav", "six.wav", "seven.wav",
                 "eight.wav", "nine.wav", "ten.wav", "eleven.wav"]
    numPicked = random.randint(0, 5)
    print(songsList[numPicked])
    return songsList[numPicked]

def meowPicker():
    meowList = ["meow0.wav", "meow1.wav", "meow2.wav", "meow3.wav", "meow4.wav"]
    numPicked = random.randint(0, 4)
    print(meowList[numPicked])
    return meowList[numPicked]
    

while True:
    if(time.time() >= start + (1*60) and wTimeFinished == False and wTimeStarted == True):         # set timer 45 min
        print("45 min end")
        wTimeFinished = True
        pygame.mixer.music.load("15min.wav")
        pygame.mixer.music.play()
        print("15 min start")
        bTimeStarted = True
        start1 = time.time()
        # set timer 15 min
    if(time.time() >= start1 + (0.5*60) and bTimeFinished == False and bTimeStarted == True):         # set timer 45 min
        #study session end
        print("15 min end")

     
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio).lower()
    print(words)
    

    if words == "today":
        print(date.today())
        
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
        pygame.mixer.music.load("song2.wav")
        pygame.mixer.music.play()
        
    if words.startswith("play song "):
        words = words.replace("play song ", "")
        
        if words == "2":
            words = "two"
        if words == "3":
            words = "three"
        if words == "for":
            words = "four"
        try:
            songReq = words + ".wav"
            pygame.mixer.music.load(songReq)
            pygame.mixer.music.play()
        
        except IOError:
             print("invalid command: ", songReq)
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

    if words.startswith("start timer for "): # eg 1 minute
	words = words.replace("start timer for ", "")
	if words == " 1 minute"
        
        

    if (words == "meow" or words == "talk" or words == "say something"):
        meowOut = meowPicker()
	pygame.mixer.music.load(meowOut)
        pygame.mixer.music.play()

    if words == "relay one on":
        relay1.on()
        
    if words == "relay one off":
        relay1.off()

    if words == "relay two on":
        relay2.on()

    if words == "relay two off":
        relay2.off()

    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Goodbye")
        break