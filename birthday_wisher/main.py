import smtplib

my_email = "matasem.test@gmail.com"
password = "h123H!@#"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="SevenMoatasem@gmail.com", msg="Hello")
connection.close()
