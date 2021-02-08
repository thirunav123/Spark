import serial
import time 
serial_rs232 = serial.Serial("/dev/ttyS0",
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.EIGHTBITS,
        timeout=1 )
while 1:
   rs_232_time_to_wait=time.time()+10
   X = serial_rs232.read()
   while time.time()<rs_232_time_to_wait:
          X = serial_rs232.read()
          if X>b'0':
             break
   #print(s)
   send_data="connected.."
   res = send_data.encode('utf-8')
   serial_rs232.write(res)
   serial_rs232.flush()  # send_byte= ''.jo(ord(i), 'b') for i in send_data)
   #print(send_byte)
   time.sleep(1)
   print(X)

