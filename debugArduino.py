import serial

# Setup...
arduino = serial.Serial('COM3', 9600)

while True:
    arduino.write(f'{input()}\r'.encode())