import pocketqube_simulator
import struct

pq = pocketqube_simulator.PocketQubeSimulator()

while 1:
    address = input('Address: ')
    instruction = input('Instruction: ')

    print(f'Response: {pq.comunication(address, instruction)}\n')
