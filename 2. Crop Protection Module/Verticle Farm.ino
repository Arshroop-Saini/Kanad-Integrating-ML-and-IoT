#include <Servo.h>
#define BUZZER_PIN 4
int light;
const int led_pin = 13;
Servo Servo1;
Servo Servo2;
int servoPin1 = 9;
int positio=0;
int servoPin2=2;
void setup() 
{
  pinMode(4,OUTPUT);
  pinMode(A2,INPUT);
  Servo1.attach(9);  
  Servo2.attach(2);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(led_pin,OUTPUT);
  Serial.begin(9600);                                                                                                                                                                                                                                                                                                                                                                 
}

void loop() 
{
  int sensorValue = analogRead(A0);
  int light=analogRead(A1);
  Serial.println(light);

  Serial.println(String(light)+" "+String(sensorValue));
 
  if (sensorValue < 500)
  {
  analogWrite(BUZZER_PIN, 50);
  digitalWrite( led_pin,HIGH);
  Servo1.write(-90);
  Servo2.write(90);
  delay(1000);
  }
  else
  {
    analogWrite(BUZZER_PIN, 0);   
    digitalWrite( led_pin , LOW); 
    Servo1.write(90);                             
    Servo2.write(-90);
    delay(1000);
  }
} 
