# Projeto de Reconhecimento de Fala e Controle de Servo Motores com Arduino - Cesar School

Este projeto visa combinar o reconhecimento de fala utilizando Python com controle de servo motores utilizando Arduino. O objetivo é permitir que comandos de voz sejam captados, reconhecidos e convertidos em sinais que controlam servos em uma placa Arduino.

## Componentes

### Componentes de Arduino
- **Placa Arduino (modelo compatível)**: Placa microcontroladora que executará o código para controlar os servos.
- **6 Servo motores**: Utilizados para realizar movimentos físicos em resposta aos comandos de voz.
- **Cabos de conexão**: Para conectar os servomotores aos pinos correspondentes na placa Arduino.

### Componentes de Python
- **Microfone**: Para captar os comandos de voz.
- **Computador com Python instalado**: A máquina que rodará o script de reconhecimento de voz.
- **Bibliotecas Python**:
  - `pyserial`: Para a comunicação serial entre o Python e o Arduino.
  - `speech_recognition`: Para converter a fala captada pelo microfone em texto.
  - `playsound`: Para reproduzir sons de feedback ou alertas, se necessário.


## Instalação

### Arduino

1. Certifique-se de ter o [Arduino IDE](https://www.arduino.cc/en/software) instalado.
2. Conecte os servos aos pinos 2, 3, 4, 5, 6 e 7 da placa Arduino.
3. Carregue o seguinte código no Arduino:

    ```cpp
    #include "Servo.h"
    #include "string.h"

    Servo servo[6];
    String speechToText;

    void setup() {
      servo[0].attach(2);
      servo[1].attach(3);
      servo[2].attach(4);
      servo[3].attach(5);
      servo[4].attach(6);
      servo[5].attach(7);
      Serial.begin(9600);
    }

    void moverPino(int pino1, int pino2, int pino3, int pino4, int pino5, int pino6) {
      int estados[] = { pino1, pino2, pino3, pino4, pino5, pino6 };
      int sobe = 90;
      int desce = 10;

      for (int i = 0; i < 6; i++) {
        if (estados[i]) {
          servo[i].write(sobe);
        } else {
          servo[i].write(desce);
        }
      }
    }

    void mapaLetras(char letra) {
      switch (letra) {
        case 'A':
          moverPino(1, 0, 0, 0, 0, 0);
          break;
        case 'B':
          moverPino(1, 0, 1, 0, 0, 0);
          break;
        case 'C':
          moverPino(1, 1, 0, 0, 0, 0);
          break;
        // Mais casos para outras letras
        case 'Z':
          moverPino(1, 0, 0, 1, 1, 1);
          break;
      }
    }

    void loop() {
      while (Serial.available() == 0) {}

      speechToText = Serial.readStringUntil('\r');
      const char* sttCast = speechToText.c_str();

      if (strstr(sttCast, "LETRA")) {
        char letra = speechToText[strlen(sttCast) - 2];
      }

      speechToText = "";
    }
    ```

### Python

1. Instale as dependências necessárias:
    ```bash
    pip install pyserial speechrecognition playsound pyaudio
    ```

2. Crie um arquivo `main.py` com o seguinte código:

    ```python
    import serial
    import speech_recognition as sr
    from playsound import playsound

    # Setup...
    arduino = serial.Serial('COM5', 9600)
    r = sr.Recognizer()

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
    ```

## Utilização

1. Conecte o Arduino ao computador.
2. Carregue o código no Arduino usando o Arduino IDE.
3. Execute o script Python:

    ```bash
    python main.py
    ```
4. Fale próximo ao microfone. O sistema reconhecerá sua fala e enviará os comandos correspondentes para o Arduino controlar os servos.

## Funcionamento do Código

### Código Arduino

O código Arduino é responsável por controlar seis servo motores baseados em comandos recebidos via comunicação serial. A seguir, a explicação das principais funções:

1. **setup():** Anexa os seis servos ao pino 5 e inicializa a comunicação serial a 9600 bps.
2. **moverPino():** Recebe seis inteiros representando os estados dos pinos e move os servos para as posições de acordo com esses estados (90 graus para cima, 10 graus para baixo).
3. **mapaLetras():** Mapeia caracteres para estados específicos dos pinos dos servos, de forma que diferentes letras resultam em diferentes posições dos servos.
4. **loop():** Aguarda por entrada serial, lê a string recebida até encontrar o caractere '\r', verifica se a string contém "LETRA", extrai a letra e limpa a string `speechToText`.

### Código Python

O código Python capta áudio do microfone, converte o áudio em texto utilizando a API do Google Speech Recognition, e envia o texto convertido ao Arduino via comunicação serial. A seguir, a explicação das principais partes:

1. **Importação de Bibliotecas:** Importa `serial` para comunicação serial, `speech_recognition` para reconhecimento de fala, e `playsound` para reprodução de áudio.
2. **Configuração Inicial:** Configura a porta serial para comunicação com o Arduino e inicializa o reconhecedor de fala.
3. **Função `reproduzir_audio()`:** Reproduz um arquivo de áudio MP3.
4. **Loop Principal:** Utiliza um loop infinito para continuamente captar e processar áudio, ajustar o nível de ruído ambiental, capturar o áudio do microfone, converter o áudio em texto utilizando a API do Google, e enviar o texto convertido ao Arduino via serial. Trata exceções específicas para erros de requisição e erros desconhecidos.


## Possíveis Melhorias

- Melhorar a precisão do reconhecimento de fala ajustando os parâmetros do microfone.
- Adicionar mais casos ao mapeamento de letras para suportar mais comandos.
- Implementar feedback auditivo ou visual para confirmar os comandos reconhecidos.

