#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
# from email.utils import parseaddr - модуль валидации email
import markdown
# нужно импортировать модуль журналирования
# модуль unittest
# модуль работы с потоками


class EmailConfig:
    """Экземпляр данного класса будет содержать настройки провадера"""

    def __init__(self, **conf):
        self.s_host = conf["s_host"]
        self.s_login = conf["s_login"]
        self.s_pass = conf["s_pass"]
        self.c_type = conf["c_type"]
        self.s_port = conf["s_port"]


class EmailSender:
    """В данном классе будет формироватся сообщение,
    в конструктор передаем основные характеристики почтового сообщения:
        -FROM:
        -TO:
        -SUBJECT:
        -POST_SRV:
        """
    def __init__(self, transport):
        self.from_adr = ""
        self.to_adr = []
        self.subject = ""
        self.transport = transport

    def send_msg(self, body):
        """Метод организующий отправку сообщений"""
        # Логика автоматической проверки типа разметки сообщения - для расширения функционала
        msg_type = "plain"
        if '<html>' in body:
            msg_type = "html"
        elif ("#" in body and "*" in body) or ("~" in body and "#" in body) or ("=" in body and ">" in body):
            body = "<html><head><title></title><body>%s</body></html>" % markdown.markdown(body)
            msg_type = "html"

        msg = MIMEText(body, msg_type)
        msg['Subject'] = self.subject
        msg['From'] = self.from_adr
        msg['To'] = ", ".join(self.to_adr)
        if self.transport.c_type == "SSL":
            server = smtplib.SMTP_SSL(self.transport.s_host, self.transport.s_port)
        else:
            server = smtplib.SMTP(self.transport.s_host, self.transport.s_port)
            server.ehlo()
            server.starttls()
            server.ehlo()
        server.login(self.from_adr, self.transport.s_pass)
        server.set_debuglevel(1)  # вывод отладочной информации, 0-выкл
        server.sendmail(self.from_adr, self.to_adr, msg.as_string())
        server.quit()


if __name__ == "__main__":
    pass
