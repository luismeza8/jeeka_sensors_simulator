import random
import struct

import pandas as pd

class PocketQubeSimulator:
    simulated_data = pd.read_csv('datos_corregidos.csv')
    iteration_data = 0
    trama = {
        'beginnig': hex(0xff),
        'source_address': hex(0xcc),
        'destination_address': None,
        'length': None,
        'rssi': None,
        'instruction': None,
        'beginnig_message': hex(0xff),
        'message': None,
        'end_message': hex(0xef),
        'end': hex(0xef)
    }

    def next_iteration(self):
        self.iteration_data += 1


    def get_orientation(self):
        gyro_x = self.simulated_data['gx'].loc[self.iteration_data]
        gyro_y = self.simulated_data['gy'].loc[self.iteration_data]
        gyro_z = self.simulated_data['gz'].loc[self.iteration_data]
        return [gyro_x, gyro_y, gyro_z]

    def get_altitude(self):
        #altitude = self.simulated_data['altura'].loc[self.iteration_data]
        altitude = -12.3
        altitude_in_hex = self.convert_float_to_hex(altitude)
        return altitude_in_hex


    def convert_float_to_ieee754(self, float_value):
        packed = struct.pack('>f', float_value)
        return ''.join(f'{byte:08b}' for byte in packed)


    def separate_binary(self, bin_str):
        bytes_separados = [bin_str[i:i+8] for i in range(0, len(bin_str), 8)]
        return bytes_separados


    def convert_binary_bytes_to_hex(self, binary):
        bytes_converted = []
        for byte in binary:
            bytes_converted.append(hex(int(byte, 2)))
        return bytes_converted


    def convert_float_to_hex(self, value):
        ieee = self.convert_float_to_ieee754(value)
        bytes_separed = self.separate_binary(ieee)
        hexs = self.convert_binary_bytes_to_hex(bytes_separed)
        return hexs



    def get_velocity(self):
        return self.simulated_data[''].loc[self.iteration_data]

    def get_acelerations(self):
        aceleration_x = self.simulated_data['ax'].loc[self.iteration_data]
        aceleration_y = self.simulated_data['ay'].loc[self.iteration_data]
        aceleration_z = self.simulated_data['az'].loc[self.iteration_data]
        return [aceleration_x, aceleration_y, aceleration_z]

    def get_temperature(self):
        temperature = self.simulated_data['temperatura'].loc[self.iteration_data]
        return temperature

    def get_pressure(self):
        pressure = self.simulated_data['presion'].loc[self.iteration_data]
        return pressure

    def get_position(self):
        return [random.uniform(-40, 40), random.uniform(-40, 40)]

    def get_battery(self):
        return random.randint(0, 100)

    def get_phase(self):
        return random.randint(0, 3)

    def get_medition(self):
        medition = self.simulated_data['medicion'].loc[self.iteration_data]
        return medition

    def get_time(self):
        time = self.simulated_data['tiempo'].loc[self.iteration_data]
        return time

    def generate_all_data(self):
        return [
            self.get_medition(),
            self.get_time(),
            self.get_altitude(),
            self.get_temperature(),
            self.get_pressure(),
            self.get_acelerations(), 
            self.get_orientation(),
            #generate_velocity(),
            self.get_position(),
            #generate_battery(),
            #generate_phase()
        ]

    instructions = {
        # Acctions
        'str': None, 
        'abr': None,
        'rst': None,
        'fin': None,
        'sig': next_iteration,
        # Data
        'med': get_medition,
        'gyr': get_orientation,
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
            self.trama['length'] = hex(len(str(self.trama['message'])))
            self.trama['rssi'] = hex(random.randint(-120, -30))

            return list(self.trama.values())

        return 'Instruction unknown'

def main():
    pq = PocketQubeSimulator()
    
    while 1:
        address = input('Address: ')
        instruction = input('Instruction: ')
    
        print(f'Response: {pq.comunication(address, instruction)}\n')

if __name__ == '__main__':
    main()

