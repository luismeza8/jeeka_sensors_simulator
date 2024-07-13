import serial
import random
import pandas as pd

class PocketQubeSimulator:
    serial_port_1 = serial.Serial('/dev/pts/6')
    csv_data = pd.read_csv('datos_corregidos.csv')
    iteration = 0

    def generate_orientation(self):
        return [self.csv_data['gx'].loc[self.iteration], self.csv_data['gy'].loc[self.iteration], self.csv_data['gz'].loc[self.iteration]]

    def generate_altitude(self):
        return self.csv_data['altura'].loc[self.iteration]

    def generate_velocity(self):
        return self.csv_data[''].loc[self.iteration]

    def generate_acelerations(self):
        return [self.csv_data['ax'].loc[self.iteration], self.csv_data['ay'].loc[self.iteration], self.csv_data['az'].loc[self.iteration]]

    def generate_temperature(self):
        return self.csv_data['temperatura'].loc[self.iteration]

    def generate_pressure(self):
        return self.csv_data['presion'].loc[self.iteration]

    def generate_position(self):
        return [random.uniform(-40, 40), random.uniform(-40, 40)]

    def generate_battery(self):
        return random.randint(0, 100)

    def generate_phase(self):
        return random.randint(0, 3)

    def get_medition(self):
        return self.csv_data['medicion'].loc[self.iteration]

    def get_time(self):
        return self.csv_data['tiempo'].loc[self.iteration]

    def generate_all_data(self):
        self.iteration += 1
        return [
            self.get_medition(),
            self.get_time(),
            self.generate_altitude(),
            self.generate_temperature(),
            self.generate_pressure(),
            self.generate_acelerations(), 
            self.generate_orientation(),
            #generate_velocity(),
            #generate_position(),
            #generate_battery(),
            #generate_phase()
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


    '''
    while True:
        if serial_port_1.in_waiting > 0:
            data = serial_port_1.readline().decode('utf-8', errors='ignore').rstrip()
            print(data)

            data_separared = data.split()
            if data_separared[0] == 'pq':
                print(f'command recived: {data_separared[1]}')
                for key, value in instructions.items():
                    if data_separared[1] == key:
                        i = key
                        m = value()
                        response = f'{hex(it)} {hex(do)} {hex(dd)} {rssi} {i} {hex(it)} {m} {hex(ft)} {hex(ft)}'
                        serial_port_1.write(b'{response}\n')
                        print(f'response: {response}\n')
                        iteration += 1
                        break
            else:
                print(data)
                print('nop')
    '''
