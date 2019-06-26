import mysql.connector
con=mysql.connector.connect(host="localhost",user="rashi",password="")
cur=con.cursor()
try:
	dbs=cur.execute("Show databases")
	print(dbs)
except:
	con.rollback()
for i in cur:
	print(i)
con.close()