import serial
import speech_recognition as sr
from playsound import playsound

# Setup...
arduino = serial.Serial('COM5', 9600)
r=sr.Recognizer()

def reproduzir_audio():
    playsound("./nome_do_arquivo.mp3")

while True:

    try:
        with sr.Microphone() as source2: # Use the microphone
             
            r.adjust_for_ambient_noise(source2, duration=0.2) # Adjust noise threshold
            
            speech = r.listen(source2, None, 2) # Listen to the mic
            
            speech_to_text = r.recognize_google(speech, language="pt-BR").upper() # Using google to recognize audio

            print("You said :", speech_to_text)

            arduino.write(f'{speech_to_text}\r'.encode())
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
