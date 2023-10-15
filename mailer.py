import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

fromaddr = 'tosyaqa@mail.ru'
toaddr = 'tosyaqa@mail.ru'
mypass = 'CjrheEChza4Q1urphfMb'

def send(subject, message):
    msg = EmailMessage()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    msg.set_content(message)

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()