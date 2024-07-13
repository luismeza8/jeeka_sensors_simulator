import requests
import serial
from time import sleep
import pocketqube_simulator

url = 'http://localhost:8000/graphs/medition'
body = {
    'medition': None,
    'time': None,
    'altitude': None,
    'temperature': None,
    'pressure': None,
    'aceleration_x': None,
    'aceleration_y': None,
    'aceleration_z': None,
    'gyro_x': None,
    'gyro_y': None,
    'gyro_z': None,
    'battery': None,
    }

pq = pocketqube_simulator.PocketQubeSimulator()

for _ in range(1000):
    data = pq.generate_all_data()

    body['medition'] = data[0]
    body['time'] = data[1]
    body['altitude'] = data[2]
    body['temperature'] = data[3]
    body['pressure'] = data[4]
    body['aceleration_x'] = data[5][0]
    body['aceleration_y'] = data[5][1]
    body['aceleration_z'] = data[5][2]
    body['gyro_x'] = data[6][0]
    body['gyro_y'] = data[6][1]
    body['gyro_z'] = data[6][2]
    body['battery'] = 99

    r = requests.get(url, body)
    print(r.text)
    sleep(0.5)


