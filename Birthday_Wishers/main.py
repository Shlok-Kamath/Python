import smtplib
import datetime

my_mail = "kamathshlok93@gmail.com"
my_password = "ykyrjjiyhugfzvwf"

connections = smtplib.SMTP("smtp.gmail.com")
connections.starttls()
connections.login(user=my_mail, password=my_password)
connections.sendmail(from_addr=my_mail, to_addrs="suvarnakamath1234@gmail.com", msg="Hello")