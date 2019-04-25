#include <Wire.h>
#include <MPU6050.h>
#include "I2Cdev.h"


MPU6050 mpu;

const int analogIn = A0;
int mVperAmp = 100; // use 100 for 20A Module and 66 for 30A Module
int RawValue= 0;
int ACSoffset = 2500; 
double Voltage = 0;
double Amps = 0;
 
void setup() 
{

 Wire.begin();
  TWBR=24;
  Serial.begin(57600);

  //Serial.println("Initialize MPU6050");

  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }


}



void loop()
{
  Vector rawAccel = mpu.readRawAccel();
  Vector normAccel = mpu.readNormalizeAccel();


  Serial.print(normAccel.XAxis);
  Serial.print(" ");
  Serial.print(normAccel.YAxis);
  Serial.print(" ");
  Serial.print(normAccel.ZAxis);
  Serial.print(" ");

  RawValue = analogRead(analogIn);
 Voltage = (RawValue / 1024.0) * 5000; // Gets you mV
 Amps = ((Voltage - ACSoffset) / mVperAmp);
 Serial.println(Amps,3); // the '3' after voltage allows you to display 3 digits after decimal point
 
 
  delay(0.01);
}
