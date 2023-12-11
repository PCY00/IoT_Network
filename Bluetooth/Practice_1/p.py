import time
import bluetooth
port = 1


#PiserverMacAddr ='b8:27:eb:78:07:27'
# PiserverMacAddr ='B8:27:EB:5C:46:7A'
PiserverMacAddr ='B8:27:EB:A3:B9:85'

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((PiserverMacAddr, port))
try:
    while True:
        
        f = open("C:/Users/kksp1/OneDrive/Desktop/blep_data/blood_pressure_02.txt", "rt")
        while True:
            row = f.readline()
            if not row: break
            message = row
            print(message)
            s.send(message.encode())
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Cleanup")