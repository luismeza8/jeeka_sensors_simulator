import requests
import serial
from time import sleep

url = 'http://localhost:8000/graphs/medition'
body = {
    'medition': 1,
    'time': None
    }

#r = requests.get(url, body)
#print(r.text)

port = serial.Serial('/dev/pts/11')
port.write(b'pq tem\n')

