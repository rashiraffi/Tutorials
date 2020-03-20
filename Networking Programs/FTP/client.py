from ftplib import FTP
import os
ftp = FTP('')
ftp.connect('localhost',1027)
ftp.login()
#ftp.cwd('temp') 

def uploadFile():
	print(os.listdir())
	filename = input("Enter the File name: ")
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))
	print("File Uploaded !!")

def downloadFile():
	ftp.retrlines('LIST')
	filename = input("Enter the file name: ")
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	print("File Downloaded !!")
	localfile.close()
print("1.Upload\t2.Download\t3.Exit")

while(True):
	n=int(input("Enter the choice: "))

	if(n==1):
		uploadFile()
	elif(n==2):
		downloadFile()
	elif(n==3):
		ftp.quit()
		break
	else:
		print("Invalid Input..!")
