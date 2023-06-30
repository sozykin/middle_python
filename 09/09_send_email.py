import smtplib, ssl

# Почтовый адрес отправителя
sender_email = 'ptn.course@yandex.ru'
# Почтовый адрес получателя
receiver_email = 'ptn.course@yandex.ru'
# Адрес почтового сервера
smtp_server = 'smtp.yandex.ru'
# Порт для защищенного соединения SSL
port = 465  
# Имя пользователя
login = 'ptn.course'

# Текст сообщения
message = """\
Subject: Email from Python
From: ptn.course@yandex.ru

Hi!

This message is sent from Python program.

--
Middle Python Course
"""

# Ввод пароля из командной строки
password = input("Введите пароль: ")


# Создание защищенного контекста TLS/SSL
context = ssl.create_default_context()

# Подключение к почтовому серверу через менеджер контекста
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    # Авторизация на сервере
    server.login('ptn.course', password)
    # Отправка письма
    server.sendmail(sender_email, receiver_email, message)