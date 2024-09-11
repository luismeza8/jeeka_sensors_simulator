import pocketqube_simulator
import struct

pq = pocketqube_simulator.PocketQubeSimulator()

print(pq.get_altitude())
"""
while 1:
    address = input('Address: ')
    instruction = input('Instruction: ')

    print(f'Response: {pq.comunication(address, instruction)}\n')
"""
