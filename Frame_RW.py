import serial
import time

ser= serial.Serial(port="/dev/ttyS0",
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS,
        timeout=0.1)


rs232_rreq=[1, 3, 0, 1]
rs485_rreq=[2, 3, 0, 1]
rs232_wreq=[1, 6, 0, 1]
rs485_wreq=[2, 6, 0, 1]
RS232_rreq = bytes(rs232_rreq)
RS485_rreq = bytes(rs485_rreq)
RS232_wreq = bytes(rs232_wreq)
RS485_wreq = bytes(rs485_wreq)
while 1:
    ser.write(RS232_rreq)
    for i in range(3):
        X=ser.read()
        a=int.from_bytes(X, byteorder='big')
        print(a)
        #time.sleep(.5)
    X=ser.read(a)
    print(X)
    rs232_data=int.from_bytes(X,byteorder='big')
    print("rs232=",rs232_data)
    
    ser.write(RS485_rreq)
    for i in range(3):
        X=ser.read()
        a=int.from_bytes(X, byteorder='big')
        print(a)
       # time.sleep(.5)
    X=ser.read(a)
    rs485_data=int.from_bytes(X,byteorder='big')
    print("rs485=",rs485_data)
    time.sleep(1)
    #break 
    