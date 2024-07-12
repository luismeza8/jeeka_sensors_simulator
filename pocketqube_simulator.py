import serial
import random
import pandas as pd

serial_port_1 = serial.Serial('/dev/pts/13')
data = pd.read_csv('datos_corregidos.csv')

#data.to_csv('datos_corregidos.csv', index=False, encoding='utf-8')

def generate_orientation():
    return [random.uniform(-20, 20), random.uniform(-20, 20), random.uniform(-20, 20)]

def generate_altitude():
    return random.randint(0, 500)

def generate_velocity():
    return random.randint(0, 120)

def generate_acelerations():
    return [random.uniform(-20, 20), random.uniform(-20, 20), random.uniform(-20, 20)]

def generate_temperature():
    return random.randint(0, 50)

def generate_pressure():
    return random.randint(1000, 1100)

def generate_position():
    return [random.uniform(-40, 40), random.uniform(-40, 40)]

def generate_battery():
    return random.randint(0, 100)

def generate_phase():
    return random.randint(0, 3)

def generate_all_data():
    return [
        generate_orientation(),
        generate_altitude(),
        generate_velocity(),
        generate_acelerations(), 
        generate_temperature(),
        generate_pressure(),
        generate_position(),
        generate_battery(),
        generate_phase()
    ]

instructions = {
    # Acctions
    'str': None, 
    'abr': None,
    'rst': None,
    'fin': None,
    # Data
    'ori': generate_orientation,
    'alt': generate_altitude,
    'vel': generate_velocity,
    'acl': generate_acelerations,
    'tem': generate_temperature,
    'pre': generate_pressure,
    'pos': generate_position,
    'bat': generate_battery,
    'pha': generate_phase,
    'all': generate_all_data,
}

it = 0xFE
l = None
do = 0xCC
dd = 0xDD
rssi = hex(random.randint(-120, -60))
i = None
m = None
ft = 0xEF

while 1:
    if serial_port_1.in_waiting > 0:
        data = serial_port_1.readline().decode('utf-8', errors='ignore').rstrip()

        data_separared = data.split()
        if data_separared[0] == 'pq':
            print(f'command recived: {data_separared[1]}')
            for key, value in instructions.items():
                if data_separared[1] == key:
                    i = key
                    m = value()
                    response = f'{hex(it)} {hex(do)} {hex(dd)} {rssi} {i} {m} {hex(ft)}'
                    print(f'response: {response}\n')
                    break
        else:
            print('nop')
