/*                                     *
****** Código em C do AlfaBraille ******
*                                     */

#include <Servo.h>
#include <string.h>

Servo servo[6];
String speechToText;

void setup() {
  servo[0].attach(5);
  servo[1].attach(5);
  servo[2].attach(5);
  servo[3].attach(5);
  servo[4].attach(5);
  servo[5].attach(5);
  Serial.begin(9600);
}

void moverPinos(char* posicoes){
  
  int sobe = 90;
  int desce = 10;
  
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
