import smtplib
import threading



def send_email(destination):
    gmail_user = "vectorious.jenkins@gmail.com"
    gmail_password = "exkjfwldilwsmrwu"

    sent_from = gmail_user

    server = "smtp.gmail.com"
    port = 587
    subject = 'Keep Alive Mail'
    body = "The docker is running ! ya tembel "
    message = 'Subject: {}\n\n{}'.format(subject, body)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(gmail_user, gmail_password)
    s.sendmail(sent_from, destination, message)
    s.quit()





def verify_connection():
    sent_to_elior = "eliorp@vectoriousmedtech.com"
    sent_to_yovel = "yovel@vectoriousmedtech.com"
    threading.Timer(60.0, verify_connection).start()
    print("Email send")
    send_email(sent_to_elior)
    send_email(sent_to_yovel)

verify_connection()
