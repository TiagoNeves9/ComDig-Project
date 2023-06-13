import serial.tools.list_ports
import serial


def arduino_setup():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portsList = []

    for onePort in ports:
        portsList.append(str(onePort))
        print(str(onePort))

    val = input("Select Port: COM")

    for x in range(0, len(portsList)):
        if portsList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(onePort)

    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()
    return serialInst


while True:
    arduino = arduino_setup()
    #command = input("Arduino Command: (ON/OFF):")
    dados = arduino.readline()
    print(dados)

