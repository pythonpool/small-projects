import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrating mic for ambient noise..")
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say Something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='en-IN')
    text1 = str(text)
    print("I think you said - '" + text1 + "'")

except sr.RequestError as e:
    print("error; {0}".format(e))

except Exception as e:
    print(e)