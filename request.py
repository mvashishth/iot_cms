import datetime
import serial
import csv
import os, sys
import pandas as pd
import numpy as np
from scipy.fftpack import fft
import requests 
import random
import time

URL = "https://iotcms.herokuapp.com/get_data"


sensor="Acc"
path ="readings.csv"
ser = serial.Serial('/dev/ttyUSB6', 230400)

i=0
while i<5:
	a=0
	b=300
	readings_array=np.array([])
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

	df=pd.DataFrame(data=readings_array)
	df['X'], df['Y'],df['Z'], df['I'] = zip(*df[0].map(lambda x: x.split(' ')))

	df['X'] = df['X'].astype(float).fillna(0.0)
	df['Y'] = df['Y'].astype(float).fillna(0.0)
	df['Z'] = df['Z'].astype(float).fillna(0.0)
	df['I'] = df['I'].astype(float).fillna(0.0)

	df['X'] = df['X'].tolist()
	df['Y'] = df['Y'].tolist()
	df['Z'] = df['Z'].tolist()
	df['I'] = df['I'].tolist()

	y_axis=np.arange(300)
	y_axis=y_axis.tolist()

	x_max=np.max(df['X'])
	y_max=np.max(df['Y'])
	z_max=np.max(df['Z'])

	x_rms= np.sqrt(np.mean(df['X']**2))
	y_rms=np.sqrt(np.mean(df['Y']**2))
	z_rms=np.sqrt(np.mean(df['Z']**2))


	x_max=float("{0:.2f}".format(x_max.tolist()))
	y_max=float("{0:.2f}".format(y_max.tolist()))
	z_max=float("{0:.2f}".format(z_max.tolist()))

	x_rms=float("{0:.2f}".format(x_rms.tolist()))
	y_rms=float("{0:.2f}".format(y_rms.tolist()))
	z_rms=float("{0:.2f}".format(z_rms.tolist()))

	x_read=abs(fft(df['X'])).tolist()
	y_read=abs(fft(df['Y'])).tolist()
	z_read=abs(fft(df['Z'])).tolist()

	PARAMS = {'x_max':x_max,'y_max':y_max,'z_max':z_max,'x_rms':x_rms,
	'y_rms':y_rms,'z_rms':z_rms,'x_read':x_read,'y_read':y_read,'z_read':z_read,'y_axis':y_axis} 
	r = requests.post(url = URL, json = PARAMS) 
	print("done")

	i=i+1

	time.sleep(5)

	



print("Finished")











