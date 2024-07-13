import serial
import random
import pandas as pd

serial_port_1 = serial.Serial('/dev/pts/13')
csv_data = pd.read_csv('datos_corregidos.csv')
iteration = 0

def generate_orientation():
    return csv_data['gx'].loc[iteration]

def generate_altitude():
    return csv_data['altura'].loc[iteration]

def generate_velocity():
    return csv_data[''].loc[iteration]

def generate_acelerations():
    return csv_data['ax'].loc[iteration]

def generate_temperature():
    return csv_data['temperatura'].loc[iteration]

def generate_pressure():
    return csv_data['presion'].loc[iteration]

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
do = 0xCC
dd = 0xDD
l = None
rssi = hex(random.randint(-120, -60))
i = None
m = None
ft = 0xEF

while True:
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
                    iteration += 1
                    break
        else:
            print('nop')
