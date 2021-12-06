#Python Sounds Project
from playsound import playsound
import time

mp3 = 'Spongebob_E_Minor.mp3'

def play():
    playsound(mp3)

def delay():
    play()
    time.sleep(2)
    play()

delay()

