import serial

serial = serial.Serial('/dev/pts/13', 9600)

while 1:
    print(serial.read())
