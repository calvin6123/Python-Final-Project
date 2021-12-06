#Python Sounds Project
from playsound import playsound
import sounddevice
from scipy.io.wavfile import write

def recording():  # Citation: https://www.youtube.com/watch?v=HT5w-HNcr5A

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

wav = recording()

def play():
    playsound(wav)

def loop():
    while