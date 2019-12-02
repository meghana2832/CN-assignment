import socket
import time
IP = "192.168.43.197"  # IP addr of machine B
PORT = 4000
count = 1
start=time.time()
while((time.time() - start) < 60): #Sending packets fro 60Sec
    print ("message:", count)
    msg="message: "+str(count)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(msg, (IP, PORT))
    count +=1
    data, addr = sock.recvfrom(1024)            #receving from machine B
    print("from device B: ",data)

