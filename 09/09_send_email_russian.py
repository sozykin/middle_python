import smtplib, ssl
from email.mime.text import MIMEText
from email.header    import Header

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
Привет!

Это сообщение отправлено из программы на Python.

--
Курс Python для продвинутых специалистов
"""

msg = MIMEText(message, 'plain', 'utf-8')
msg['Subject'] = Header('Привет от Python!', 'utf-8')
msg['From'] = sender_email 
msg['To'] = receiver_email 

# Печать текста сообщения в том виде
# как оно будет передаваться по сети
# print("Текст сообщения:")
# print(msg.as_string())

# Ввод пароля из командной строки
password = input("Введите пароль: ")


# Создание защищенного контекста TLS/SSL
context = ssl.create_default_context()

# Подключение к почтовому серверу через менеджер контекста
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    # Ружим отладки сетевого протокола SMTP
    # server.set_debuglevel(1)    
    # Авторизация на сервере
    server.login('ptn.course', password)
    # Отправка письма
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Письмо отправлено!")