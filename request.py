#importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://localhost:7002/get_data"
  
# location given here 
location = "delhi technological university"
 
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location,'Hello':'6541'} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 


'''import json
import requests
data = {'temperature':'24.3'}
data_json = json.dumps(data)
payload = {'json_payload': data_json }
r = requests.get("http://localhost:7002/get_data", data=payload)'''