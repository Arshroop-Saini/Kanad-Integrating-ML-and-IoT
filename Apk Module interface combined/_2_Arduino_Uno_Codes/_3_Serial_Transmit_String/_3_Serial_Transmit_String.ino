// Arduino Uno
// Transmits a string to PC 
// Rahul.S

// (c) www.xanthium.in 2021
// Tutorial - https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial
int sunlight_level=10;

int Rain_level=500;

String sunlight_level_string;
String Rain_level_string;
String text_to_send;
void setup()
{
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps 8N1

}

void loop()
{
  
 sunlight_level_string= String(sunlight_level); 
Rain_level_string=String(Rain_level);

text_to_send=sunlight_level_string+" "+Rain_level_string;
  Serial.println(text_to_send); // sends a \n with text
  delay(1000);
}
      

  
