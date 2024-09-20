import random
import struct

import pandas as pd

class PocketQubeSimulator:
    simulated_data = pd.read_csv('datos_corregidos.csv')
    iteration_data = 0
    divisor = '101010101'
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
        'crc': None,
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
        altitude = 0.012345
        altitude_in_hex = self.convert_float_to_hex(altitude)
        return ' '.join(altitude_in_hex)


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
        '0x01': get_medition,
        '0x02': get_orientation,
        '0x03': get_altitude,
        '0x04': get_velocity,
        '0x05': get_acelerations,
        '0x06': get_temperature,
        '0x07': get_pressure,
        '0x08': get_position,
        '0x09': get_battery,
        '0x0A': get_phase,
        '0x0B': generate_all_data,
    }


    def xor_division(self, dividend, divisor):
        dividend = list(map(int, dividend))
        divisor = list(map(int, divisor))
        len_divisor = len(divisor)

        for i in range(len(dividend) - len_divisor + 1):
            if dividend[i] == 1:
                for j in range(len_divisor):
                    dividend[i + j] ^= divisor[j]

        remainder = dividend[-(len_divisor - 1):]
        
        return ''.join(map(str, remainder))


    def get_binary_dividend_for_crc(self, message):
        binary_message = ''
        message_bytes = message.split(' ')
        for i in message_bytes:
            byte_dec = int(i, 16)
            binary = bin(byte_dec)[2:]
            binary_message += binary

        dividend = binary_message + '0' * (len(self.divisor) - 1)

        return dividend
    

    def calculate_crc(self, message):
        binary = self.get_binary_dividend_for_crc(message)
        crc = self.xor_division(binary, self.divisor)
        return hex(int(crc, 2))


    def fill_trama(self, instruction):
        try:
            if instruction in self.instructions.keys():
                self.trama['instruction'] = instruction
                self.trama['message'] = self.instructions[instruction](self)
                self.trama['length'] = hex(len(str(self.trama['message'])))
                self.trama['rssi'] = hex(random.randint(-120, -30))
                self.trama['crc'] = self.calculate_crc(self.trama['message'])
        except:
            print('Instruction unknown')


    def comunication(self, address, instruction):
        self.trama['destination_address'] = address
        self.fill_trama(instruction)

        return ' '.join(list(self.trama.values()))


def main():
    pq = PocketQubeSimulator()
    
    while 1:
        address = input('Address: ')
        instruction = input('Instruction: ')
    
        print(f'Response: {pq.comunication(address, instruction)}\n')

if __name__ == '__main__':
    main()

