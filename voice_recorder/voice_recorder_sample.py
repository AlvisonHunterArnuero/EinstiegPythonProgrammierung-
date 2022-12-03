import sounddevice as sd
from scipy.io.wavfile import write


# Establish the sample rate for this recording
fs = 44100

# Request recording time from the user
seconds = int(input("Please enter recording time in seconds: "))

# Request the name of the recording
recording_name = input("Please enter recording file name: ") or "MyRecording"

print("We are now recording... \n")
record_voice = sd.rec(int(seconds*fs), samplerate=fs,channels=2)
sd.wait()

write("recording_name.wav", fs, record_voice)

print("All done! Recorded File can be found within this app folder.")

