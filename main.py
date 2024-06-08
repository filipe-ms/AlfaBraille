import serial
import random
import time
import speech_recognition as sr
from playsound import playsound


# Setup...
arduino = serial.Serial('COM3', 9600)
r=sr.Recognizer()

def reproduzir_audio(audio): # Função para reprodução de audio com python
    match audio:
        case 'A':
            playsound.playsound("./AlfaBraille/audios/letra_a.wav")
        case 'B':
            playsound.playsound("./AlfaBraille/audios/letra_b.wav")
        case 'C':
            playsound.playsound("./AlfaBraille/audios/letra_c.wav")
        case 'D':
            playsound.playsound("./AlfaBraille/audios/letra_d.wav")
        case 'DÊ':
            playsound.playsound("./AlfaBraille/audios/letra_d.wav")
        case 'E':
            playsound.playsound("./AlfaBraille/audios/letra_e.wav")
        case 'Ê':
            playsound.playsound("./AlfaBraille/audios/letra_e.wav")
        case 'F':
            playsound.playsound("./AlfaBraille/audios/letra_f.wav")
        case 'G':
            playsound.playsound("./AlfaBraille/audios/letra_g.wav")
        case 'GÊ':
            playsound.playsound("./AlfaBraille/audios/letra_g.wav")
        case 'H':
            playsound.playsound("./AlfaBraille/audios/letra_h.wav")
        case 'I':
            playsound.playsound("./AlfaBraille/audios/letra_i.wav")
        case 'J':
            playsound.playsound("./AlfaBraille/audios/letra_j.wav")
        case 'JOTA':
            playsound.playsound("./AlfaBraille/audios/letra_j.wav")
        case 'K':
            playsound.playsound("./AlfaBraille/audios/letra_k.wav")
        case 'CÁ':
            playsound.playsound("./AlfaBraille/audios/letra_k.wav")
        case 'L':
            playsound.playsound("./AlfaBraille/audios/letra_l.wav")
        case 'ELE':
            playsound.playsound("./AlfaBraille/audios/letra_l.wav")
        case 'M':
            playsound.playsound("./AlfaBraille/audios/letra_m.wav")
        case 'N':
            playsound.playsound("./AlfaBraille/audios/letra_n.wav")
        case 'O':
            playsound.playsound("./AlfaBraille/audios/letra_o.wav")
        case 'P':
            playsound.playsound("./AlfaBraille/audios/letra_p.wav")
        case 'Q':
            playsound.playsound("./AlfaBraille/audios/letra_q.wav")
        case 'QUE':
            playsound.playsound("./AlfaBraille/audios/letra_q.wav")
        case 'QUÊ':
            playsound.playsound("./AlfaBraille/audios/letra_q.wav")
        case 'R':
            playsound.playsound("./AlfaBraille/audios/letra_r.wav")
        case 'S':
            playsound.playsound("./AlfaBraille/audios/letra_s.wav")
        case 'ESSE':
            playsound.playsound("./AlfaBraille/audios/letra_s.wav")
        case 'T':
            playsound.playsound("./AlfaBraille/audios/letra_t.wav")
        case 'U':
            playsound.playsound("./AlfaBraille/audios/letra_u.wav")
        case 'V':
            playsound.playsound("./AlfaBraille/audios/letra_v.wav")
        case 'VÊ':
            playsound.playsound("./AlfaBraille/audios/letra_v.wav")
        case 'W':
            playsound.playsound("./AlfaBraille/audios/letra_w.wav")
        case 'X':
            playsound.playsound("./AlfaBraille/audios/letra_x.wav")
        case 'Y':
            playsound.playsound("./AlfaBraille/audios/letra_y.wav")
        case 'Z':
            playsound.playsound("./AlfaBraille/audios/letra_z.wav")

def to_braille(letra): # Função para mapear os pinos que o arduino vai levantar para a representação em braille
      match letra:
        case 'A': return ('10' +
                          '00' +
                          '00')
        
        case 'B': return ('10' +
                          '10' +
                          '00')
          
        case 'C': return ('11' +
                          '00' +
                          '00')
          
        case 'D': return ('11' +
                          '01' +
                          '00')
          
        case 'DÊ': return ('11' +
                           '01' +
                           '00')
          
        case 'E': return ('10' +
                          '01' +
                          '00')
          
        case 'Ê': return ('10' +
                          '01' +
                          '00')
          
        case 'F': return ('11' +
                          '10' +
                          '00')
          
        case 'G': return ('11' +
                          '11' +
                          '00')
          
        case 'GÊ': return ('11' +
                          '11' +
                          '00')
          
        case 'H': return ('10' +
                          '11' +
                          '00')
           
        case 'I': return ('01' +
                          '10' +
                          '00')
          
        case 'J': return ('01' +
                          '11' +
                          '00')
          
        case 'JOTA': return ('01' +
                             '11' +
                             '00')
          
        case 'K': return ('10' +
                          '00' +
                          '10')
          
        case 'CÁ': return ('10' +
                           '00' +
                           '10')
        
        case 'L': return ('10' +
                          '10' +
                          '10')
        
        case 'ELE': return ('10' +
                            '10' +
                            '10')
          
        case 'M': return ('11' +
                          '00' +
                          '10')
          
        case 'N': return ('11' +
                          '01' +
                          '10')
          
        case 'O': return ('10' +
                          '01' +
                          '10')
          
        case 'P': return ('11' +
                          '10' +
                          '10')
          
        case 'Q': return ('11' +
                          '11' +
                          '10')
          
        case 'QUE': return ('11' +
                            '11' +
                            '10')
        
        case 'QUÊ': return ('11' +
                            '11' +
                            '10')
          
        case 'R': return ('10' +
                          '11' +
                          '10')
          
        case 'S': return ('01' +
                          '10' +
                          '10')
        
        case 'ESSE': return ('01' +
                             '10' +
                             '10')
        
          
        case 'T': return ('01' +
                          '11' +
                          '10')
          
        case 'U': return ('10' +
                          '00' +
                          '11')
          
        case 'V': return ('10' +
                          '10' +
                          '11')
          
        case 'VÊ': return ('10' +
                           '10' +
                           '11')
          
        case 'W': return ('01' +
                          '11' +
                          '01')
          
        case 'X': return ('11' +
                          '00' +
                          '11')
          
        case 'Y': return ('11' +
                          '01' +
                          '11')
          
        case 'Z': return ('10' +
                          '01' +
                          '11')
          
        case _: 
            print("Letra não reconhecida.")

def speech_to_text(): # Função que capta o input do microfone e retorna como string
    try:
        with sr.Microphone() as source2: # Use the microphone
            r.adjust_for_ambient_noise(source2, duration=0.2) # Adjust noise threshold
            speech = r.listen(source2, 5, 5) # Listen to the mic
            speech_to_text = r.recognize_google(speech, language="pt-BR").upper() # Using google to recognize audio
            print("You said :", speech_to_text)
            return speech_to_text

    except sr.RequestError as e:
        print("Requisição falhou: {0}".format(e))
         
    except sr.UnknownValueError:
        print("Aguardando...")

gamemode = 'aprendizado' # Modo de funcionamento default
stt = ''

while True:
    while gamemode == 'aprendizado': # Quando em modo de aprendizado...
        lista = list(map(chr, (range(65, 90))))
        lista_comandos = ['SIM', 'PRÓXIMA', 'MODO DESAFIO', 'MODO SELEÇÃO']
        for i in lista:
            stt = ''
            while stt not in lista_comandos:
                print(f'letra {i}') # GRAVAR ISSO
                arduino.write(f'{to_braille(i)}\r'.encode())

                time.sleep(2)

                print('proxima?') # GRAVAR ISSO
                
                stt = speech_to_text()
                if stt == '' or stt == None:
                    while stt == '' or stt == None:
                        # GRAVAR NÃO OUVI
                        stt = speech_to_text()
                        print(stt)


            if stt == 'SIM' or stt == 'PRÓXIMA':
                continue
            elif stt == 'MODO DESAFIO':
                gamemode = 'desafio'
                break
            elif stt == 'MODO SELEÇÃO':
                gamemode = 'seleção'
                break
            else:
                print('não entendi')

    while gamemode == 'desafio': # Quando em modo de teste...
        playsound.playsound("./AlfaBraille/audios/modo_teste_ativado.wav")
        #print('Modo teste ativo') # GRAVAR ISSO
        lista_comandos = ['MODO APRENDIZADO', 'MODO SELEÇÃO']

        while stt not in lista_comandos:
            lista = list(map(chr, (range(65, 90))))
            letra_aleatoria = random.choice(lista)

            print(letra_aleatoria)
            arduino.write(f'{to_braille(letra_aleatoria)}\r'.encode())
            
            print('Que letra') # GRAVAR ISSO
            time.sleep(2)

            stt = speech_to_text()

            if stt == '' or stt == None:
                while stt == '' or stt == None:
                    stt = speech_to_text()
                    playsound.playsound("./AlfaBraille/audios/nao_entendi.wav") # GRAVAR NÃO OUVI // TÁ EMBAIXO PARA DEBUG
            
            elif stt == 'MODO APRENDIZADO':
                gamemode = 'aprendizado'
                break
            elif stt == 'MODO SELEÇÃO':
                gamemode = 'seleção'
                break

            guess = stt.split()
            print(guess)
            print("^ GUESS")
            
            if guess[0] == 'LETRA' and len(guess[1]) == 1:
                if guess[1] == letra_aleatoria:
                    playsound.playsound("./AlfaBraille/audios/acertou.wav")
                else:
                    playsound.playsound("./AlfaBraille/audios/errou.wav")
            else:
                print('Não entendi! Tenta essa outra:')
                time.sleep(2)
        
    while gamemode == 'seleção':
        stt = ''
        print('que letra') # GRAVAR ISSO
        lista_comandos = ['MODO APRENDIZADO', 'MODO DESAFIO']

        while stt not in lista_comandos:
            stt = speech_to_text()
            if stt == '' or stt == None:
                while stt == '' or stt == None:
                    stt = speech_to_text()
                    playsound.playsound("./AlfaBraille/audios/nao_entendi.wav")

            letra = stt.split()
            time.sleep(2)

            if letra[0]=='LETRA' and len(letra[1])==1:
                arduino.write(f'{to_braille(letra[1])}\r'.encode())
