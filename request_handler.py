import requests
from time import sleep
import pocketqube_simulator

url = 'http://localhost:8000/medition'
pq = pocketqube_simulator.PocketQubeSimulator()

while True:
    data = pq.generate_all_data()
    body = {
        'medition': data[0],
        'time': data[1],
        'altitude': data[2],
        'temperature': data[3],
        'pressure': data[4],
        'aceleration_x': data[5][0],
        'aceleration_y': data[5][1],
        'aceleration_z': data[5][2],
        'gyro_x': data[6][0],
        'gyro_y': data[6][1],
        'gyro_z': data[6][2],
        'battery': 99,
        }

    r = requests.get(url, body)
    print(r.text)
    sleep(0.2)


