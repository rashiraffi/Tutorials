import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=12346
data=[]
k=int(input("Enter the Number of packet: "))
sock.sendto(str(k).encode(),("127.0.0.1",port))
print("Enter Data")
for i in range (1,k+1):
  data.append(input())
  sock.sendto(str(data[i-1]).encode(),("127.0.0.1",port))
  print(str(i),"th Packet sent..")
print("Transmission Finished..")

while(True):
  dt=sock.recvfrom(1024)[0]
  j=int(dt.decode())
  if(j==-1):
    print("Invalid packet number")
    break
  print(str(j),"th packet corrupted\nRetransmitting from ",str(j),"th packet")
  for i in range (j-1,k):
    sock.sendto(data[i].encode(),("127.0.0.1",port))
    print(str(i+1),"th Packet Retransmitted..")
  break
sock.close()

