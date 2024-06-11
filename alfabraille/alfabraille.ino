/*                                     *
****** Código em C do AlfaBraille ******
*                                     */

#include <Servo.h>
#include <string.h>

Servo servo[6];
String speechToText;

void setup() {
  for (int i = 0; i < 6; i++) {
    servo[i].write(posicaobaixo(i));
  }

  servo[0].write(posicaobaixo(0));

  servo[0].attach(3);
  servo[1].attach(5);
  servo[2].attach(6);
  servo[3].attach(9);
  servo[4].attach(10);
  servo[5].attach(11);

  servo[0].write(55);



  Serial.begin(9600);
}


int posicaocima(int pos) {
  switch (pos) {
    case 0:
      return 110;
    case 1:
      return 85;
    case 2:
      return 85;
    case 3:
      return 85;
    case 4:
      return 85;
    case 5:
      return 95;
  }
}

int posicaobaixo(int pos) {
  switch (pos) {
    case 0:
      return 55;
    case 1:
      return 50;
    case 2:
      return 25;
    case 3:
      return 25;
    case 4:
      return 25;
    case 5:
      return 25;
  }
}

void moverPinos(char* posicoes) {

  int desce = 25;

  for (int i = 0; i < 6; i++) {
    if (posicoes[i] == '1') {
      servo[i].write(posicaocima(i));
    } else {
      servo[i].write(posicaobaixo(i));
    }
  }
}

void loop() {
  while (Serial.available() == 0) {}

  speechToText = Serial.readString();
  char* sttCast = speechToText.c_str();
  moverPinos(sttCast);
  speechToText = "";
}
