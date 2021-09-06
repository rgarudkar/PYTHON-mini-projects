import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "My@gmail.com"  # Enter your address
receiver_email = "Your@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """Subject: Email by python

My first email sent using python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)






