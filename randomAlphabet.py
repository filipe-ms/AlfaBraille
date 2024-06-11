import serial

import random
import time

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

# Setup...
arduino = serial.Serial('COM3', 9600)
lista = list(map(chr, (range(65, 90))))

while True:
    lst_item = random.choice(lista)
    arduino.write(f'{to_braille(lst_item)}\r'.encode())
    print(lst_item)
    time.sleep(2)