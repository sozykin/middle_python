import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

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

message = MIMEMultipart("alternative")
message["Subject"] = Header('Сообщение в HTML', 'utf-8')
message["From"] = sender_email
message["To"] = receiver_email

# Текстовое сообщение
text = """\
Привет!

Это сообщение отправлено из программы на Python.

--
Курс Python для продвинутых специалистов
"""

# Сообщение в HTML
html = """\
<html>
  <body>
    <p>Привет!<br>
    Это сообщение отправлено из <strong>программы на Python</strong>.   
    </p>
    --
    <p>Курс <a href='https://github.com/sozykin/middle_python'>Python для продвинутых специалистов</a>.</p>
  </body>
</html>
"""

# Создаем две части сообщения в MIMEText
part1 = MIMEText(text, "plain", 'utf-8')
part2 = MIMEText(html, "html", 'utf-8')

# Добавляем текстовое и HTML сообщение
message.attach(part1)
message.attach(part2)

# Печать текста сообщения в том виде
# как оно будет передаваться по сети
# print("Текст сообщения:")
# print(message.as_string())

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
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Письмо отправлено!")