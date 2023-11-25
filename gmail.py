import email
from email.message import EmailMessage
import smtplib
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)

    gmail_user = '1ms17ml022@gmail.com'
    gmail_password  = 'eneni'
    msg['subject'] = subject
    msg['From'] = '1ms17ml022@gmail.com'
    msg['To'] = to

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.send_message()
    s.quit()

if __name__ == '__main__':
    email_alert("Test", "https://discord.gg/cAWW5qq","3095824273@vtext.com")
