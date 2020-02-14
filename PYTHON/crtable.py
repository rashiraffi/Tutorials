import mysql.connector
con=mysql.connector.connect(host="localhost",user="rashi",password="",database="demo")
cur=con.cursor()
try:
	dbs=cur.execute("create table Employee(name varchar(20) not null, id int(2) not null primary key, salary int(6) not null)")
	dbs1=cur.execute("show tables")
except:
	con.rollback()
for i in cur:
	print(i)
con.close()