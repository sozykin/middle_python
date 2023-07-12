import asyncio
import time
from aiohttp import ClientSession, TCPConnector
import logging


async def get_vacancy(id, session):
    url = f'/vacancies/{id}'
    
    logging.debug(f"Начата загрузка вакансии {url}")

    async with session.get(url=url) as response:
        vacancy_json = await response.json()
        logging.debug(f"Завершена загрузка вакансии {url}")
        return vacancy_json


async def main(ids):
    # Ограничиваем количество максимальных подключений
    connector = TCPConnector(limit=5)
    async with ClientSession('https://api.hh.ru/', connector=connector) as session:
        tasks = []
        for id in ids:
            tasks.append(asyncio.create_task(get_vacancy(id, session)))

        results = await asyncio.gather(*tasks)

    for result in results:
        print(result['name'], result['employer']['name'])


# Настройка логгера
logging.basicConfig(filename='my_app.log', 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")

vacancies_ids = ['82247456', '82347857', '82373818', '81867563',
                 '81780083', '82135615', '81949300', '81330856',
                 '82104952', '82054624', '81941871', '82260854']

start = time.time()

asyncio.run(main(vacancies_ids ))

print("Время выполнения, с: ", time.time() - start)
