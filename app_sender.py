#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email_sender import EmailConfig
from email_sender import EmailSender
"""В целях безопасности почтовые адреса и пароли хранятся за пределами кода,
 для прозрачности блоки обращения к файлам можно заменить на примеры в комментариях.
 ПРИМЕР:
 mail_ru = EmailConfig(s_host="smtp.mail.ru",
                    s_login="foo@mail.ru",
                    s_pass="fooPassword",
                    c_type="SSL",
                    s_port=465)
"""

# Конфигурация для провайдера mail.ru
inbox = EmailConfig(s_host="smtp.inbox.ru",
                    s_login=open("D:\\PWD\\mail.txt").readlines()[0].strip(),
                    s_pass=open("D:\\PWD\\pass.txt").readlines()[0].strip(),
                    c_type="SSL",
                    s_port=465)

# Конфигурация для провайдера gmail.com
gmail = EmailConfig(s_host="smtp.gmail.com",
                    s_login=open("D:\\PWD\\mail.txt").readlines()[1].strip(),
                    s_pass=open("D:\\PWD\\pass.txt").readlines()[1].strip(),
                    c_type="SSL",
                    s_port=465)

# Конфигурация для провайдера yandex.ru
yandex = EmailConfig(s_host="smtp.yandex.ru",
                    s_login=open("D:\\PWD\\mail.txt").readlines()[2].strip(),
                    s_pass=open("D:\\PWD\\pass.txt").readlines()[2].strip(),
                    c_type="SSL",
                    s_port=465)

# Конфигурация для провайдера hotmail.com
hotmail = EmailConfig(s_host="smtp.live.com",
                    s_login=open("D:\\PWD\\mail.txt").readlines()[3].strip(),
                    s_pass=open("D:\\PWD\\pass.txt").readlines()[3].strip(),
                    c_type="TTL",
                    s_port=587)

# Формируем заголовок сообщения
mail_01 = EmailSender(inbox)  # указываем экземпляр класса с настройками соответствующего провайдера
# в это свойство передается адрес отправителя, можно указать явно "foo@mail.ru" или извлечь из переданного экземпляра
mail_01.from_adr = mail_01.transport.s_login
# в это свойство передается список получателей
mail_01.to_adr = [x.strip() for x in open("D:\\PWD\\mail.txt").readlines()]  # извлекаю список адресатов
mail_01.subject = "Тестовое сообщение"

# Варианты сообщений с разным типом разметки
text_ascii = open("D:\\PWD\\text_ascii.txt").read()
text_simple = open("D:\\PWD\\text_simple.txt").read()
html = open("D:\\PWD\\html.htm").read()
markdown = open("D:\\PWD\\markdown.txt").read()
# Выполняю отправку
mail_01.send_msg(text_simple)
