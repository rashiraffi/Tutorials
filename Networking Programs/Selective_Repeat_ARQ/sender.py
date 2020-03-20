import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
	port=12346
	data=[]
	n=int(input("Enter the number of packet: "))
	sock.sendto(str(n).encode(),("127.0.0.1",port))
	print("Enter Data")
	for i in range (1,n+1):
		data.append(input())
		sock.sendto(data[i-1].encode(),("127.0.0.1",port))
		print(str(i),"th Packet sent..")
	print("Transmission Finished..")
	j=int((sock.recvfrom(1024)[0]).decode())        
	if(j!=-1):
		print(str(j),"th packet corrupted\nRetransmitting ",str(j),"th packet")
		sock.sendto(data[j-1].encode(),("127.0.0.1",port))
		print(str(j),"th Packet Retransmitted..")
		print("Data Sent Sucessfully...")
	else:
		print("Invalid packet number")
except Exception as e:
	print(e)
	sock.close()