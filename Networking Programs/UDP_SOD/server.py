import socket
def sop(num):
    s=0
    while(num!=0):
        s=s+(num%10)
        num=num//10
    return str(s)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',8006))
    print("Server started..!")
    while(True):
        data, addr = sock.recvfrom(1024)
        if(data.decode()=="close"):
            print("Terminated..!")
            sock.close()
            break
        data=int(data.decode())
        msg=sop(data)
        sock.sendto(msg.encode(),addr)
except Exception as e:
    print("Error..!",e)
    sock.close()