import os
import smtplib

import json

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class sendMessageToGmail():
    mail = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_CODE')

    def __init__(self):
        self.msg = MIMEMultipart()

    def create_message(self, description, message):
        self.msg['Subject'] = description
        self.msg['From'] = self.mail
        self.msg['To'] = self.mail

        body_part = MIMEText(message, 'plain')
        self.msg.attach(body_part)

    def send_message(self):
        smtp_obj = smtplib.SMTP('smtp.gmail.com')

        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.ehlo()

        smtp_obj.login(self.mail, self.password)

        smtp_obj.sendmail(self.msg['From'],
                          self.msg['To'], self.msg.as_string())
        smtp_obj.quit()


def generate_message(data):
    '''Данный метод пишется специально под определённые задачи'''

    _, name, last_name, email, phone, title = data.values()

    return f'Имя: {name}\nФамилия: {last_name}\nemail: {email}\nТелефон: {phone}\nНазвание номера: {title}'


def generate_message_registration(data):
    data = list(data.values())

    return f'Название комнаты: {data[1]}\nДата заезда: {data[2]}.{data[3]}.{data[4]}\nДата выезда: {data[5]}.{data[6]}.{data[7]}\nemail: {data[-1]}'
