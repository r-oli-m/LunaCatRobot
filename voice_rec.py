import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep
import pygame
import random

red = LED(17)
relay1 = LED(14)
relay2 = LED(15)

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")
pygame.mixer.init()

def songPicker():
    songsList = ["song0.wav", "song1.wav", "song2.wav", "song3.wav",
                 "song4.wav", "song5.wav", "song6.wav", "song7.wav",
                 "song8.wav", "song9.wav", "song10.wav", "song11.wav"]
    numPicked = random.randint(0, 5)
    print(songsList[numPicked])
    return songsList[numPicked]
    

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    

    if words == "today":
        print(date.today())
        
    if words == "Play song":
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
        pygame.mixer.music.rewind()
       
    if words == "volume lower":
        newVol = pygame.mixer.music.get_volume() - 0.35
        pygame.mixer.music.set_volume(newVol)
        
    if words == "volume higher":
        newVol = pygame.mixer.music.get_volume() + 0.35
        pygame.mixer.music.set_volume(newVol)

    if words == "LED on":
        red.on()

    if words == "LED off":
        red.off()

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