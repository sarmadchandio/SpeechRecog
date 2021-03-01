import speech_recognition as sr
import sys
# This program converts Speech to text using google speech recognition

if len(sys.argv) != 2:
    print("format --> python SpeechRecognition 'filename.ext'")
    exit(1)


r = sr.Recognizer()
filename = sys.argv[1]
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)


