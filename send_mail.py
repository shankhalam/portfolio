import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "dev.shankhalam@gmail.com"
password = "fjpxntlortzxjurr"

receiver = "dev.shankhalam@gmail.com"
message = """\
Subject: Test Mail.
Hai Shan Khalam, this is test mail.Thank you.
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)