import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "" #Enter Your mail address
toaddr = "" #Enter To Address
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "" # Enter the subject
body = "For testing my SMTP server"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, "********") #Enter your PASSWORD
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Mail Sent Successfully!")
server.quit()