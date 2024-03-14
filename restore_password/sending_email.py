import smtplib
from email.mime.text import MIMEText


def send_email(user_email, s_code):
    port = 587
    smtp_google = 'smtp.gmail.com'
    sender = 'asd91124@gmail.com'
    password = 'nefsrqwurpswrhrq'
    server = smtplib.SMTP(smtp_google, port)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(str(s_code))
        msg['Subject'] = 'Secret code'
        msg['To'] = user_email
        server.sendmail(sender, user_email, msg.as_string())
        server.quit()
        return 'отправлено'
    except Exception as ex:
        print('EX: ', ex)