import aiohttp
import asyncio

# Создаем native coroutine
async def main():
    # Контекст менеджер with в асинхронном режиме
    async with aiohttp.ClientSession() as session:
        async with session.get('http://msk.rt.ru/') as response:

            print("Статус ответа:", response.status)

            html = await response.text()
            print("Тело сообщения:", html[:120], "...")

# Запускаем native coroutine main с помощью 
# библиотеки asyncio
asyncio.run(main())