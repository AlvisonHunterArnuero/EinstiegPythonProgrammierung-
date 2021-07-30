# ------------------------------------------------------------------------
# Convert an amount of Text to Speech as an audio file(mp3) using Python 3
# Made with ❤️ in Python 3 by Alvison Hunter - July 7th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ------------------------------------------------------------------------

# Import the required module for text to speech conversion
from gtts import gTTS
# This module will allow us to play the generated mp3 file in the end
import subprocess

# This will be the text that you want to convert to audio
mytext = '''
Hi, people! My name is Alvison and I am from Nicaragua. In my everyday life, I work
as a web programmer using several languages such as JavaScript, VBA, C sharp and PYTHON.
From all of these languages, the one I love to work and code with the most is Python.
'''
# Language in which you want the audio to sound like
language = 'en'

# Passing the text and language to the engine, we've marked slow=False.
# Which tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, tld='com', slow=False)

# This variable will contain the name of the audio file
audio_file = "languages_audio.mp3"

# Saving the converted audio in a mp3 file named languages_audio
print("Saving file. Please wait...")
myobj.save(audio_file)

# Inform the user that the file has been generated without any issues
print(f"File {audio_file} has been successfully saved.")

# Let's play and listen to this new audio file now, shall we?
return_code = subprocess.call(["afplay", audio_file])
print("Done playing the generated audio. Thanks for listening, don't forget to subscribe!")
