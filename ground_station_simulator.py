from pocketqube_simulator import PocketQubeSimulator
import struct

pq = PocketQubeSimulator()


altitude = pq.get_altitude()
hexs = []

class GroundStationSimulator:
    def convert_hex_to_float(self, hex):
        hexs = []
        for byte in hex:
            byte_dec = int(byte, 16)
            byte_bin = bin(byte_dec)[2:]
            
            # si el byte empieza por ceros python no los cuenta, entonces lo siguiente agrega esos ceros faltantes 
            if len(byte_bin) < 8:
                difference = 8 - len(byte_bin)
                zeros = '0' * difference
                byte_bin = f'{zeros}{byte_bin}'

            hexs.append(byte_bin)

        final = ''.join(hexs)
        final = int(final, 2)

        flotante = struct.unpack('>f', struct.pack('>I', final))[0]
        return flotante

gs = GroundStationSimulator()
print(gs.convert_hex_to_float(altitude))

"""
while 1:

    pq_data = pq.comunication('0xff', 'all')
    print(f'Trama en crudo del PocketQube: {pq_data}')

    pq_beginnig = pq_data[0]
    print(f'Inicio: {int(pq_beginnig, 0)}')

    pq_source_address = pq_data[1]
    print(f'Direccion fuente: {int(pq_source_address, 0)}')

    pq_destination_address = pq_data[2]
    print(f'Direccion destino: {int(pq_destination_address, 0)}')

    pq_length = pq_data[3]return ''.join(f'{byte:08b}' for byte in packed)
    print(f'largo: {int(pq_length, 0)}')

    pq_rssi = pq_data[4]
    print(f'rssi: {int(pq_rssi, 0)}')

    pq_instruction = pq_data[5]
    print(f'instruccion: {pq_instruction}')

    pq_message = pq_data[7]
    print(f'mensaje: {pq_message}')

    pq_medition = pq_message[0]
    print(f'medicion: {pq_medition}')
    pq_time = pq_message[1]
    print(f'tiempo: {pq_time}')
    pq_altitude = pq_message[2]
    print(f'altitud: {pq_altitude}')
    pq_temperature = pq_message[3]
    pq_pressure = pq_message[4]
    print(f'temperatura: {pq_temperature}')
    pq_acelerations = pq_message[5]
    print(f'aceleraciones x y z: {pq_acelerations}')
    pq_orientations = pq_message[6]
    print(f'gyros x y z: {pq_orientations}')

    pq_end = pq_data[9]
    print(f'fin: {int(pq_end, 0)}')

    print('\n')

    pq.next_iteration()
    sleep(0.5)
"""
