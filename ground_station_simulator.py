from pocketqube_simulator import PocketQubeSimulator
from time import sleep

pq = PocketQubeSimulator()

while 1:

    pq_data = pq.comunication('0xff', 'all')
    print(f'Trama en crudo del PocketQube: {pq_data}')

    pq_beginnig = pq_data[0]
    print(f'Inicio: {int(pq_beginnig, 0)}')

    pq_source_address = pq_data[1]
    print(f'Direccion fuente: {int(pq_source_address, 0)}')

    pq_destination_address = pq_data[2]
    print(f'Direccion destino: {int(pq_destination_address, 0)}')

    pq_length = pq_data[3]
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
