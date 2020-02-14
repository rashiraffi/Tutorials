import mysql.connector
con=mysql.connector.connect(host="localhost",user="rashi",password="",database="demo")
c=con.cursor()
try:
	c.execute("select * from student")
	res=c.fetchall()
	#print(res)
	re1=res[0]
	print(re1[1])
	for i in res:
		print("%d %s %s %s"%(i[0],i[1],i[2],i[3]))
except:
	con.rollback()

con.close()