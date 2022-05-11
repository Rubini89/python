import requests
import json
import re


url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'
print ("API call started")
response = requests.get (url)
print ("API response stored in response.xml file") 
#print (response.content)
data1 = json.loads(response.content)
with open("response.json", "w") as f:
    f.write(str(data1))


length = len(data1)
print(length)
 
