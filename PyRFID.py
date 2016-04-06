import serial

port = serial.Serial("/dev/cu.usbserial-AI03WO5A", baudrate=9600, timeout=None)

while True:
    rcv = port.readline()
    print rcv+"\n"
