import socket
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Enter close to terminate")
    while(True):
        msg=input("Enter the digit: ")
        sock.sendto(msg.encode(),('127.0.0.1',8006))
        if(msg=='close'):
            print("Terminated..!")
            sock.close()
            break
        data, addr = sock.recvfrom(1024)
        print("Sum of digit = " + data.decode())
except Exception as e:
    print("Error..!", e)
    sock.close()