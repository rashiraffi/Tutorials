import time
tim=time.localtime(time.time())
print("Hours:%d Minutes:%d Second:%d"%(tim[3],tim[4],tim[5]))
for i in tim:
	print(i)
	time.sleep(1)
