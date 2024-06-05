/*                                     *
****** Código em C do AlfaBraille ******
*                                     */

#include <Servo.h>
#include <string.h>

Servo servo[6];
String speechToText;

void setup() {
  servo[0].attach(3);
  servo[1].attach(5);
  servo[2].attach(6);
  servo[3].attach(9);
  servo[4].attach(10);
  servo[5].attach(11);
  
  for(int i=0; i<6; i++){
    servo[i].write(20);
  }

  Serial.begin(9600);
}

void moverPinos(char* posicoes){
  
  int sobe = 80;
  int desce = 20;
  
  for(int i=0; i<6; i++){
    if(posicoes[i]=='1'){
      servo[i].write(sobe);
    } else {
      servo[i].write(desce);
    }
  }
}

void loop() {
  while(Serial.available()==0){}
  
  speechToText = Serial.readStringUntil('\r');
  char* sttCast = speechToText.c_str();
  moverPinos(sttCast);
  speechToText="";
}
