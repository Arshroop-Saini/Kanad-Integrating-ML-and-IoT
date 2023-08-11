#include <LiquidCrystal.h>

int pump = 7;
int uppervalue_dry=950;
int uppervalue_humid=500;
int uppervalue_wet=400;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void(* resetFunc) (void) = 0;
void setup()
{
  pinMode(7, OUTPUT); 
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(A2, INPUT);
}
void loop()
{
  digitalWrite(7, LOW);

  int SensorValue= analogRead(A2);

  int percentValue = map(SensorValue, 1023, 200, 0, 100);
    Serial. println(SensorValue);
  delay(1000);
    lcd.setCursor(0, 0);
  lcd.print("Auto-Irrigation");
  lcd.setCursor(10,1);
  lcd.print("Module");  
delay(1000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Soil Moisture");
  delay(1000);
  lcd.setCursor(0,1);
  lcd.print(SensorValue);
   Serial. println(SensorValue);
  delay(1000);
  lcd.clear();

  if(SensorValue >= uppervalue_dry) 
{
  lcd.setCursor(0, 0);
  lcd.print("Sensor");
  lcd.setCursor(4,1);
  lcd.print("Not in soil");
  }
  if(SensorValue < uppervalue_dry && SensorValue >=uppervalue_humid ) 
{ 
   lcd.setCursor(0,0);
   lcd.print("SOIL CONDITION:");
   delay(1000);
   lcd.setCursor(0,1);
   lcd.print("DRY");
  }
  if(SensorValue < uppervalue_humid && SensorValue >= uppervalue_wet) 
{
   lcd.setCursor(0,0);
   lcd.print("SOIL CONDITION:");
   delay(1000);
     lcd.setCursor(0,1);
   lcd.print("HUMID");
  }
  if(SensorValue < uppervalue_wet) 
{
   lcd.setCursor(4,0);
   lcd.print("Alert!!");
   lcd.setCursor(0,1);
   lcd.print("Too Much Water!!");
  }
delay(1000);
lcd.clear();
     if(SensorValue<uppervalue_dry&&SensorValue>=uppervalue_humid){
    
      lcd.print("PUMP:On ");
  
      digitalWrite(7, HIGH);

      delay(5000);
      digitalWrite(7, LOW);
      delay(2000);
      resetFunc();
     }
     else if(SensorValue>uppervalue_dry)
        {digitalWrite(pump, LOW);
         lcd.print("PUMP:Off ");
         

      }
         else if(SensorValue<uppervalue_humid&&SensorValue>=uppervalue_wet)
        {digitalWrite(pump, LOW);
         lcd.print("PUMP:Off ");

         

      }
      else if(SensorValue<500&&SensorValue>=0)
       {digitalWrite(pump, LOW);
        lcd.print("PUMP:Off ");
      
     }
  delay(1000);

  lcd.clear();

}