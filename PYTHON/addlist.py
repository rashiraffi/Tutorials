a=[]
while(True):
	print("1. ADD")
	print("2. Remove")
	print("3. Print")
	c=int(input("\nEnter the choice: "))
	if (c==1):
		n=int(input("\nEnter the number: "))
		a.append(n)
	elif (c==2):
		r=int(input("\nEnter the number to remove: "))
		a.remove(r)
	elif(c==3):
		print("\n",a)
	else:
		print("Wrong input....")
