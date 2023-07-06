import logging

url = 'https://api.hh.ru/vacancies/82247456'

# Настройка логгера
logging.basicConfig(filename='my_app.log', 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

logging.debug(f'Начата загрузка вакансии {url}')