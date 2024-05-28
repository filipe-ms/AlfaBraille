# AlfaBraille 
# Projeto de Reconhecimento de Fala e Controle de Servo Motores com Arduino - Cesar School 🎤🤖

Este projeto visa combinar o reconhecimento de fala utilizando Python com controle de servo motores utilizando Arduino. O objetivo é permitir que comandos de voz sejam captados, reconhecidos e convertidos em sinais que controlam servos em uma placa Arduino.

## Componentes 🛠️

- Placa Arduino (modelo compatível)
- 6 Servo motores
- Microfone (para entrada de voz)
- Computador com Python instalado
- Biblioteca `pyserial` para comunicação serial
- Biblioteca `speech_recognition` para reconhecimento de fala
- Biblioteca `playsound` para reprodução de áudio

## Instalação 📦

### Arduino

1. Certifique-se de ter o [Arduino IDE](https://www.arduino.cc/en/software) instalado.
2. Conecte os servos aos pinos 2, 3, 4, 5, 6 e 7 da placa Arduino.
3. Carregue o código do Arduino disponível no repositório no Arduino.

    O código do Arduino se encontra no arquivo `arduino_code.ino`. Este código configura os pinos dos servos, define a lógica para controlar os servos com base em comandos recebidos via comunicação serial e mapeia letras para estados específicos dos pinos dos servos.

### Python

1. Instale as dependências necessárias:
    ```bash
    pip install pyserial speechrecognition playsound pyaudio
    ```

2. Crie um arquivo `main.py` e copie o código Python disponível no repositório.

    O código Python está no arquivo `main.py`. Este código capta áudio do microfone, converte o áudio em texto utilizando a API do Google Speech Recognition, e envia o texto convertido ao Arduino via comunicação serial. Ele também inclui uma função para reproduzir um arquivo de áudio MP3.

## Utilização 🚀

1. Conecte o Arduino ao computador.
2. Carregue o código no Arduino usando o Arduino IDE.
3. Execute o script Python:

    ```bash
    python main.py
    ```
4. Fale próximo ao microfone. O sistema reconhecerá sua fala e enviará os comandos correspondentes para o Arduino controlar os servos.

## Funcionamento do Código ⚙️

### Código Arduino

O código Arduino é responsável por controlar seis servo motores baseados em comandos recebidos via comunicação serial. A seguir, a explicação das principais funções:

1. **setup():** Configura os pinos dos servos e inicializa a comunicação serial.
2. **moverPino():** Recebe seis inteiros representando os estados dos pinos e move os servos para as posições de acordo com esses estados (90 graus para cima, 10 graus para baixo).
3. **mapaLetras():** Mapeia caracteres para estados específicos dos pinos dos servos, de forma que diferentes letras resultam em diferentes posições dos servos.
4. **loop():** Aguarda por entrada serial, lê a string recebida até encontrar o caractere '\r', verifica se a string contém "LETRA", extrai a letra e limpa a string `speechToText`.

### Código Python

O código Python capta áudio do microfone, converte o áudio em texto utilizando a API do Google Speech Recognition, e envia o texto convertido ao Arduino via comunicação serial. A seguir, a explicação das principais partes:

1. **Importação de Bibliotecas:** Importa `serial` para comunicação serial, `speech_recognition` para reconhecimento de fala, e `playsound` para reprodução de áudio.
2. **Configuração Inicial:** Configura a porta serial para comunicação com o Arduino e inicializa o reconhecedor de fala.
3. **Função `reproduzir_audio()`:** Reproduz um arquivo de áudio MP3.
4. **Loop Principal:** Utiliza um loop infinito para continuamente captar e processar áudio, ajustar o nível de ruído ambiental, capturar o áudio do microfone, converter o áudio em texto utilizando a API do Google, e enviar o texto convertido ao Arduino via serial. Trata exceções específicas para erros de requisição e erros desconhecidos.
