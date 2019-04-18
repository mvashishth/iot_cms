#importing the requests library 
import requests 
import random
import time
import numpy as np
# api-endpoint 
URL = "http://localhost:7002/get_data"
  
# location given here 

while 1>0:
	x_read = np.random.uniform(low=1, high=100.3, size=(3000,)) #check here. Can't make this array bigger than 300 elements
	y_read = np.random.uniform(low=1, high=10.3, size=(3000,))
	z_read = np.random.uniform(low=1, high=40.3, size=(3000,))
	y_axis=np.arange(3000)
	x_max=np.max(x_read)
	y_max=np.max(y_read)
	z_max=np.max(z_read)
	x_rms= np.sqrt(np.mean(x_read**2))
	y_rms=np.sqrt(np.mean(y_read**2))
	z_rms=np.sqrt(np.mean(z_read**2))

	x_read = x_read.tolist()
	y_read = y_read.tolist()
	z_read = z_read.tolist()
	y_axis=y_axis.tolist()
	x_max=float("{0:.2f}".format(x_max.tolist()))
	y_max=float("{0:.2f}".format(y_max.tolist()))
	z_max=float("{0:.2f}".format(z_max.tolist()))
	x_rms=float("{0:.2f}".format(x_rms.tolist()))
	y_rms=float("{0:.2f}".format(y_rms.tolist()))
	z_rms=float("{0:.2f}".format(z_rms.tolist()))
	z=random.randint(10,100)
	dummy=[1,2,3]
	PARAMS = {'x_max':x_max,'y_max':y_max,'z_max':z_max,'x_rms':x_rms,
	'y_rms':y_rms,'z_rms':z_rms,'x_read':x_read,'y_read':y_read,'z_read':z_read,'y_axis':y_axis} 
	r = requests.post(url = URL, json = PARAMS) 
	print("done")
	print(type(x_read))
	print(type(dummy))

	time.sleep(5)
