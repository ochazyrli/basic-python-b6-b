#Pelatihan Basic Python Indonesia.Ai
#Zyrlirosa - 081287980257
#Final Project

# Sumber Coding 
# https://realpython.com/python-send-email/

import smtplib, ssl

email = open("receiver_list.txt", "r")
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "kevrvng@gmail.com"  # Enter your address
receiver_email = email.readlines()  # Enter receiver address
password = input("Type your password and press enter: ")


message = """\
Subject: Final Project!

This message is sent from Python
alias
YEEE BISAA!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message )