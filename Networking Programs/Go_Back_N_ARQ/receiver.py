import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=12346
sock.bind(("127.0.0.1",port))
data,addr=sock.recvfrom(1024)
j=int(data.decode())
print("# Data")
for i in range(1,j+1):
	data,addr=sock.recvfrom(1024)
	print(str(i),":",data.decode())
c=int(input("Enter the corrupted packet number: "))
if(c==0 or c>int(j)):
	sock.sendto(str(-1),addr)
	print("Invalid packet number")
else:
	sock.sendto(str(c).encode(),addr)
	print("# Data")
	for i in range (c,j+1):
		dt=sock.recvfrom(1024)[0]
		print(str(i),":",dt.decode())
sock.close()
