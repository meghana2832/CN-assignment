import socket
IP = "192.168.43.95"             #ip addr of machine A
PORT = 4000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))
while True:
    data, addr = sock.recvfrom(1024)            #recv udp packets from A
    print ("received message from A:", data)
    msg= "received message:"+str(data) 
    sock.sendto(msg, (IP, PORT))       #send packets to machine A
