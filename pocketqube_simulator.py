import random

import pandas as pd

class PocketQubeSimulator:
    simulated_data = pd.read_csv('datos_corregidos.csv')
    iteration_data = 0
    trama = {
        'beginnig': hex( 0xff ),
        'source_address': hex( 0xcc ),
        'destination_address': None,
        'lenght': None,
        'rssi': random.randrange(-120, -30),
        'instruction': None,
        'message': None,
        'end': hex( 0xef )
    }

    def get_orientation(self):
        gyro_x = self.simulated_data['gx'].loc[self.iteration_data]
        gyro_y = self.simulated_data['gy'].loc[self.iteration_data]
        gyro_z = self.simulated_data['gz'].loc[self.iteration_data]
        self.iteration_data += 1
        return [gyro_x, gyro_y, gyro_z]

    def get_altitude(self):
        altitude = self.simulated_data['altura'].loc[self.iteration_data]
        self.iteration_data += 1
        return altitude

    def get_velocity(self):
        return self.simulated_data[''].loc[self.iteration_data]

    def get_acelerations(self):
        aceleration_x = self.simulated_data['ax'].loc[self.iteration_data]
        aceleration_y = self.simulated_data['ay'].loc[self.iteration_data]
        aceleration_z = self.simulated_data['az'].loc[self.iteration_data]
        self.iteration_data += 1
        return [aceleration_x, aceleration_y, aceleration_z]

    def get_temperature(self):
        temperature = self.simulated_data['temperatura'].loc[self.iteration_data]
        self.iteration_data += 1
        return temperature

    def get_pressure(self):
        pressure = self.simulated_data['presion'].loc[self.iteration_data]
        self.iteration_data += 1
        return pressure

    def get_position(self):
        return [random.uniform(-40, 40), random.uniform(-40, 40)]

    def get_battery(self):
        return random.randint(0, 100)

    def get_phase(self):
        return random.randint(0, 3)

    def get_medition(self):
        medition = self.simulated_data['medicion'].loc[self.iteration_data]
        self.iteration_data += 1
        return medition

    def get_time(self):
        time = self.simulated_data['tiempo'].loc[self.iteration_data]
        self.iteration_data += 1
        return time

    def generate_all_data(self):
        self.iteration_data += 1
        return [
            self.get_medition(),
            self.get_time(),
            self.get_altitude(),
            self.get_temperature(),
            self.get_pressure(),
            self.get_acelerations(), 
            self.get_orientation(),
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
        'ori': get_orientation,
        'alt': get_altitude,
        'vel': get_velocity,
        'acl': get_acelerations,
        'tem': get_temperature,
        'pre': get_pressure,
        'pos': get_position,
        'bat': get_battery,
        'pha': get_phase,
        'all': generate_all_data,
    }

    def comunication(self, address, instruction):
        if instruction in self.instructions.keys():
            self.trama['destination_address'] = address
            self.trama['instruction'] = instruction
            self.trama['message'] = self.instructions[instruction](self)
            self.trama['lenght'] = hex(len(str( self.trama['message'] )))

            return self.trama.values()

        return 'Instruction unknown'
