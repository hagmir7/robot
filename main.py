# pip install speechRecognition
import  datetime
import speech_recognition as sr
import  pywhatkit

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print('See something...')
        audio = recorder.listen(source)
    text = recorder.recognize_google(audio)
    print(f'You sed : {text}')
    return text

text = get_audio()

if text == 'Cortana what is the date':
    print(datetime.date.today())
elif 'YouTube' in text:
    pywhatkit.playonyt(text)
    print(text)

elif "search" in text:
    for item in text:
        if item == 'Cortana' or 'Youtub' or 'search':
            item = ''
    pywhatkit.search(text)
