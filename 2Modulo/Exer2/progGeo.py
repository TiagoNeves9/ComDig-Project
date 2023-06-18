import serial.tools.list_ports
import time
import AuxFunctions as aux

arduino = aux.arduinoSetup()

while True:
    while arduino.inWaiting() == 0:
        pass
    dataPacket = arduino.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    print(dataPacket)
