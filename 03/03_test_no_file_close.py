import os

f = open('test.txt', 'w', encoding='UTF-8')
f.write('Тестовая запись в файл')

os._exit(1)