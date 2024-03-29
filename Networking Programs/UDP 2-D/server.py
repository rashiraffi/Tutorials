import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',8006))
    print("Server started..!")
    while(True):
        data, addr = sock.recvfrom(1024)
        print(addr[0] + " : " + data.decode())
        if(data.decode()=="bye"):
            print("Terminated..!")
            sock.close()
            break
        msg=input("Enter the message: ")
        sock.sendto(msg.encode(),addr)
        if(msg=='bye'):
            print("Terminated..!")
            sock.close()
            break
except:
    print("Error..!")
    sock.close()