import time
import requests


def get_vacancy(id):
    url = f'https://api.hh.ru/vacancies/{id}'
    
    response = requests.get(url)
    return response.json()


def main(ids):
    results = []
    for id in ids:
        results.append(get_vacancy(id))

    for result in results:
        print(result['name'], result['employer']['name'])


vacancies_ids = ['82247456', '82347857', '82373818', '81867563',
                 '81780083', '82135615', '81949300', '81330856',
                 '82104952', '82054624', '81941871', '82260854']

start = time.time()

main(vacancies_ids)

print("Время выполнения, с: ", time.time() - start)
