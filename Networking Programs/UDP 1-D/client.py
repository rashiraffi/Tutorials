import socket
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while(True):
        msg=input("Enter the message: ")
        sock.sendto(msg.encode(),('127.0.0.1',8004))
        if(msg=='bye'):
            print("Terminated..!")
            sock.close()
            break
except:
    print("Error..!")
    sock.close()