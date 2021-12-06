#Python Sounds Project
from playsound import playsound
import sounddevice
from scipy.io.wavfile import write

print("Hi, welcome to python audio recorder and looper!")
print("Using this program you can record your voice or any sound through a microphone and save it as a .wav file")
print("First enter how many seconds you would like to record, and there will be further instructions teaching you how to loop and playback the audio")


def recording():  # Citation: https://www.youtube.com/watch?v=HT5w-HNcr5A
    global audiofile
    fps = 44100
    duration = int(input("How many seconds would you like to record?"))

    print("Recording in progress...")
    recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=1)
    sounddevice.wait()
    print("Recording Done!")

    #create file
    filename = input("Create a filename!")
    audiofile = filename + ".wav"
    write(audiofile, fps, recording)
    return audiofile

audiofile = ""
wav = audiofile



def play(wav):
    playsound(wav)


def loop(wav):
    numOfLoops = int(input("How many times do you want to loop?"))
    for loops in range(numOfLoops):
        play(wav)

def main():

    wav = recording()

    validKeys = ["p", "P", "q", "Q", "l", "L","r","R"]
    valid = True
    while valid:
        inp = input("Enter l or L to loop, enter p or P to play, and enter q or Q to quit,")
        while inp not in validKeys:
            print("Entered invalid key")
            inp = input("Enter l/L to loop, p/P to play, r/R to amke a new recording, and q/Q to quit")
        if inp == "l" or inp == "L":
            loop(wav)
        elif inp == "P" or inp == "p":
            play(wav)
        elif inp == "r" or inp == "R":
            wav = recording()
        elif inp == "Q" or inp == "q":
            print("Thanks for using audio my python audio recorder and looper, see ya!")
            valid = False
main()






