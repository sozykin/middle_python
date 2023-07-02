import smtplib, ssl
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

message = MIMEMultipart()
message["Subject"] = Header('Сообщение с прилагаемым файлом', 'utf-8')
message["From"] = sender_email
message["To"] = receiver_email

# Сообщение в HTML
html = """\
<html>
  <body>
    <p>Привет!<br>
    Это сообщение отправлено из <strong>программы на Python</strong>.   
    </p>
    <p>В прилагаемом файле <a href='https://peps.python.org/pep-0020/'>Дзен Python</a>.</p>
    --
    <p>Курс <a href='https://github.com/sozykin/middle_python'>Python для продвинутых специалистов</a>.</p>
  </body>
</html>
"""

# Вставляем тело сообщения
message.attach(MIMEText(html, 'html', 'utf-8'))

# Имя прилагаемого файла
filename = "zen_of_python.pdf"  

# Читаем файл в бинарном режиме
with open(filename, "rb") as attachment:
    # Добавляем файл как application/octet-stream
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Кодируем файл кодировкой ASCII для отправки в email    
encoders.encode_base64(part)

# Добавляем заголовок к прилагаемому файлу
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Добавляем прилагаемый файл к сообщению
message.attach(part)

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