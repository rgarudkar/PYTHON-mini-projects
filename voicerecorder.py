import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=1)
    sounddevice.wait()
    write(file, 44100, recording) #creates uncompressed .WAV file of 10 seconds of 
    print("Recording Finished")

voice_recorder(10, "record2.wav")