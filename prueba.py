from time import sleep
import serial

ps = serial.Serial('/dev/pts/18')

while 1:
    ps.write(b'yeap\n')
    sleep(0.5)


