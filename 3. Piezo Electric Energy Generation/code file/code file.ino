int sensor=A2;
int threshold=200;
int led=4;

void setup()
{
  pinMode(4, OUTPUT); 
  Serial.begin(9600);
  pinMode(A2, INPUT);
}
void loop()
{
 int value=analogRead(sensor);
  Serial.println(value);
  if(value<=threshold)
  {
    digitalWrite(4,HIGH);
    Serial.println(value);
    }
  else
  {
  digitalWrite(4,LOW);
  Serial.println(value);
  }
}