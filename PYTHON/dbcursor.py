import mysql.connector
con=mysql.connector.connect(host="localhost",user="rashi",passwd="",database="demo")
c=con.cursor()
print(c)