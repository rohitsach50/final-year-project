#include <dht.h>

//#include <dht.h>


dht DHT;

#define DHT11_PIN 7
int moistersensor=A0;
int lightSensor=A1;
int motor = 13;
unsigned char inttensity1 = 0;
unsigned char moister1 = 0;
int temp = 0;
int hum = 0;
 int moister = 0;
 int intensity = 0;
char txPkt[50] = {0};
int cycledelay = 0; 
void setup(){
  Serial.begin(9600);
   pinMode(motor, OUTPUT); 
 // Serial.println("testing");
}

void loop()
{
 
  temp= DHT.temperature;
  hum = DHT.humidity;
//  txPkt[0] = DHT.temperature;
//  txPkt[0] = DHT.humidity;
  
  moister = analogRead(moistersensor); 
  moister  = map(moister, 0, 1023,100, 0);
  intensity = analogRead(lightSensor); 
  intensity  = map(intensity, 0, 1023, 0, 100);
  sprintf(txPkt,"field1:%3d,field2:%3d,field3:%3d,field4:%3d-",temp,hum,moister,intensity);
  
if(++cycledelay>5)
{
  for(int i=0; i <45;i++)
      Serial.write(txPkt[i]);
      
      Serial.println();
      cycledelay = 1;
}
  
  
  if(moister <50)
  {
    digitalWrite(motor, HIGH);
  }
  else
  {
    digitalWrite(motor, LOW);
  }
  int chk = DHT.read11(DHT11_PIN);
//  Serial.print("Temperature = ");
//  Serial.println(DHT.temperature);
//  Serial.print("Humidity = ");
//  Serial.println(DHT.humidity);
     delay(1000);
}



