#include <Servo.h>


Servo servoBase;
Servo servoAlejar;
Servo servoAltura;
Servo servoPinza;

int pinBase = 4; //base
int pinAlejar = 7; // alejar acercar
int pinAltura = 9; // altura 
int pinPinza = 12; //pinzas


int pinza = 80;
int base = 100;
int altura = 50;
int alejar = 50;


int a=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servoBase.attach(pinBase);
  servoAlejar.attach(pinAlejar);
  servoAltura.attach(pinAltura);
  servoPinza.attach(pinPinza);
  servoBase.write(base);
  servoAlejar.write(alejar);
  servoAltura.write(altura);
  servoPinza.write(pinza);
  
}

void loop() {
  
  if (Serial.available()){
       a=Serial.read()-'0'; 

       if(a>=0){
           Serial.print("en inicio con el valor ");
           Serial.println(a);
    
         if(a==4){
          Serial.println("IZQUIERDA");
          if(base<171){
            base=base+2;
            servoBase.write(base);
            Serial.println(base);
            delay(150);
          }
        }
        else if(a==6){
          Serial.println("DERECHA");
          if(base>9){
            base=base-2;
            servoBase.write(base);
            Serial.println(base);
            delay(150);
          }
        }
        else if(a==8){
          Serial.println("ARRIBA");
          if(altura<152){
            altura=altura+2;
            servoAltura.write(altura);
            Serial.println(altura);
            delay(150);
          }
        }
        else if(a==2){
          Serial.println("ABAJO");
           if(altura>12){
            altura=altura-2;
            servoAltura.write(altura);
            Serial.println(altura);
            delay(150);
          }
        }
        else if(a==7){
          Serial.println("ADELANTE");
          if(alejar<140){
            alejar=alejar+2;
            servoAlejar.write(alejar);
            Serial.println(alejar);
            delay(150);
          }
        }
        else if(a==1){
          Serial.println("ATRAS");
          if(alejar>12){
            alejar=alejar-2;
            servoAlejar.write(alejar);
             Serial.println(alejar);
            delay(150);
          }
        }
        else if(a==9){
          Serial.println("CERRANDO PINZAS");
          if(pinza<100){
            pinza=pinza+2;
            servoPinza.write(pinza);
             Serial.println(pinza);
            delay(150);
          }
        }
        else if(a==3){
          Serial.println("ABRIENDO PINZAS");
          if(pinza>50){
            pinza=pinza-2;
            servoPinza.write(pinza);
             Serial.println(pinza);
            delay(150);
          }
        }
        
        delay(100);
       }
  }
  
  /**/
  

}
