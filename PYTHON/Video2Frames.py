import cv2
n=input("Enter The path")
s=input("Enter the name")
cap= cv2.VideoCapture(n)
i=0
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == False:
		break
	if i%10==0:
		cv2.imwrite(s+str(i/10)+'.jpg',frame)
	i+=1
cap.release()
cv2.destroyAllWindows()