import random
n=random.randint(1,100)
while(True):
	f=int(input("Enter any number: "))
	if (f==n):
		print("You are correct...")
		break
	else:
		print("Try again..",n)
		if f>n:
			p=f-n
			print(p)
		else:
			p=n-f
			print(p)
		p=(p//10)
		print(p)
		print("You are %d percentage correct"%(100-p))

