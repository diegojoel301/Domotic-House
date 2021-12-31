import speech_recognition as sr
import webbrowser as web
from gtts import gTTS
import os
def procesar_texto(myText):
    language = 'es'

    output = gTTS(text = myText, lang = language, slow = False)

    output.save("output.mp3")
    os.system("mpg123 output.mp3")
    os.system("rm -r output.mp3")


def escuchar_voz():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Por favor di algo:")

        audio = r.listen(source)

        procesar_texto("Reconociendo")

        try:
            dest = r.recognize_google(audio)
            print("Tu dijiste:"+dest)
            procesar_texto("Tu dijiste:"+dest)
            return dest.lower()
        except Exception as e:
            procesar_texto("Hubo un error")
            print("Error:"+str(e))
    procesar_texto("Hubo un error")
    return "NULL"

if __name__ == "__main__":
    while True:
        escuchar_voz()