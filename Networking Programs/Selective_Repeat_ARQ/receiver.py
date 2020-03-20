import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
	port=12346
	sock.bind(("127.0.0.1",port))
	data,addr=sock.recvfrom(1024)
	n=int(data.decode())
	print("# Data")
	for i in range(1,n+1):
		data,addr=sock.recvfrom(1024)
		print(str(i),":",data.decode())
	print("Enter the no.of corrupted packet")
	j=int(input("Enter the corrupted packet number: "))
	if(j==0 or j>n):
		sock.sendto(str(-1),addr)
		print("Invalid packet number")
	else:
		sock.sendto(str(j).encode(),addr)
		print("# Data")
		dt=sock.recvfrom(1024)[0]
		print(str(j)," ",dt.decode())
		print("Data Recived Sucessfully..")
except Exception as e:
	print(e)
	sock.close()