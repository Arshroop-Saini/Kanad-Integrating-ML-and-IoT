int buzzer = 13;
int pump = 7;
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup()
{
  pinMode(10, OUTPUT);
  pinMode(buzzer,OUTPUT);   
  Serial.begin(9600);
    lcd.begin(16, 2);
  pinMode(A2, INPUT); 
}
void loop()
{
 
  int SensorValue= analogRead(A1);
  int percentValue = map(SensorValue, 1023, 200, 0, 100);
Serial.println(SensorValue);
delay(100);
}