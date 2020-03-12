import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('',8002))
    sock.listen(5)
    print("server Started")
    conn,addr=sock.accept()
    while(True):
        if(conn):
            data=input("Type a message to client: ")
            conn.send(data.encode())
            if(data=="Bye" or data=="bye"):
                print("Socket closed...!")
                break
except Exception as e:
    print("Error")
    sock.close()
sock.close()
