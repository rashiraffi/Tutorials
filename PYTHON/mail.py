#!/usr/bin/python3  
import smtplib  
sender_mail = 'techietraveller247@gmail.com'  
receivers_mail = ['rashi1281@gmail.com']  
message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. 
"""%(sender_mail,receivers_mail)
print("Try")
try:  
   password = 'techie123';
   print("1") 
   smtpObj = smtplib.SMTP('gmail.com',587)  
   print("2")
   smtpobj.login(sender_mail,password)
   print("3")
   smtpObj.sendmail(sender_mail, receivers_mail, message)
   print("Successfully sent email")  
except Exception:  
   print("Error: unable to send email")  