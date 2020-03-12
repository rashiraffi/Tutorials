import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8002))
print("Conncted to the server"+str(sock.getpeername))
while(True):
    data=sock.recv(1024)
    if(data):
        print(data.decode())
        if(data.decode()=="Bye" or data.decode()=="bye"):
            print("Connection closed..!")
            break
sock.close()