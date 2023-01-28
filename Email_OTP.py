import smtplib #The Main module to send a email
import secrets # will generate OTP for us
from email.message import EmailMessage # This will help us to provid a subject name to the email
#import smtplip library for sending emails
seder="sender email" # provide the sender email in this field
id="key" # provide the key if you dont know how to get it then check the Readme.md file
#sender has been defined
#let's generate otp
otp_number=secrets.token_hex(3)
message=EmailMessage()
message["Subject"]="give the subject" # provide here the required Subject
otp_message=f"your login  otp is--{otp_number} " \
            f"kindly don't share it with anyone....."
print("provide the reciver email")
reciver=input()
#let's send the email
obj=smtplib.SMTP("smtp.gmail.com",587)
obj.starttls()
obj.login(seder,id)
obj.sendmail(seder,reciver,f"{message},{otp_message}")
print(f"done the otp is-- {otp_number}")
obj.quit()