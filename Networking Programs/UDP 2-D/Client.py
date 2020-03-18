import socket
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(True):
        msg=input("Enter the message: ")
        sock.sendto(msg.encode(),('127.0.0.1',8006))
        if(msg=='bye'):
            print("Terminated..!")
            sock.close()
            break
        data, addr = sock.recvfrom(1024)
        print(addr[0] + " : " + data.decode())
        if(data.decode()=="bye"):
            print("Terminated..!")
            sock.close()
            break
except:
    print("Error..!")
    sock.close()