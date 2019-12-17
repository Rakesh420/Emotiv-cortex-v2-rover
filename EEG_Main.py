import json
from websocket import create_connection
import ssl
import time
import requests

ws = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})
#Approve app
ws.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "requestAccess",
    "params": {
        "clientId": "xxx", # The client id of your Cortex application
        "clientSecret": "xxx" # The client secret of your Cortex application
    }
}))
result = ws.recv()
result_dic = json.loads(result)

#Authorise and generate token
ws.send(json.dumps({
    "id": 4,
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": {
        "clientId": "xxx", # The client id of your Cortex application
        "clientSecret": "xxx", # The client secret of your Cortex application
    }
}))
result = ws.recv()
result_dic = json.loads(result)
auth = result_dic['result']['cortexToken']
print("---------------------- >Authorised")

#Create session
ws.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "createSession",
    "params": {
        "cortexToken": auth,
        "headset": "INSIGHT-XXXXXXXX",
        "status": "active"
    }
}))
result = ws.recv()
result_dic = json.loads(result)
print('create session result ', json.dumps(result_dic, indent=4))
session_id = result_dic['result']['id']

#Load profile form cortexApp
ws.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "setupProfile",
    "params": {
        "cortexToken": auth,
        "headset": "INSIGHT-XXXXXXXX",
        "profile": "rovereeg",
        "status": "load"
    }
}))
print(ws.recv())

#stream data from device
ws.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "cortexToken": auth,
        "session": session_id,
        "streams": ["com"]
    }
}))
print('\n')
print(ws.recv())
    
while True:
    mental_command = json.loads(ws.recv())["com"][0]
    print(mental_command) 
     
    if(thought == 'push'):
        url_get = 'http://192.168.43.198:5000/forward'
        res = requests.get(url_get)   
    elif(thought == 'left'):
        url_get = 'http://192.168.43.198:5000/pivot_left'
        res = requests.get(url_get)
    elif(thought == 'right'):    
        url_get = 'http://192.168.43.198:5000/pivot_right'
        res = requests.get(url_get)
    elif(thought == 'neutral'):    
        url_get = 'http://192.168.43.198:5000/stop_rover'
        res = requests.get(url_get)
    
   
   
	



