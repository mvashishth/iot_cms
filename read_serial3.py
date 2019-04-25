import datetime
import serial
import csv
import os, sys
import pandas as pd
import numpy as np
sensor="Acc"
path ="readings.csv"
ser = serial.Serial('/dev/ttyUSB1', 57600)

print("Initializing")

i=0
while i<5:
	readings_array=np.array([])

	a=0
	b=300
	dt_started = datetime.datetime.utcnow()
	while a<b:
		
		try:
		
			line=ser.readline()
			line=line.rstrip()
			line=line.decode()
			print(line)
			readings_array=np.append(readings_array, line)
			print("Appended")
			a=a+1



		except:
			
			pass

	dt_ended = datetime.datetime.utcnow()
	total_time=str((dt_ended - dt_started).total_seconds())
	print((dt_ended - dt_started).total_seconds())
	pd.DataFrame(readings_array).to_csv("file_time_"+total_time+"_creation_date_"+str(dt_ended)+".csv")
	i=i+1












