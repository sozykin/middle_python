# Подключаем библиотеку asyncio
import asyncio

# Создаем native coroutine
async def main():
    print('Hello ...')
    # Указываем, что выполнение следующей команды может 
    # быть приостановлено и запущена другая native coroutine
    await asyncio.sleep(1)
    print('... World!')

# Запускаем native coroutine main с помощью 
# библиотеки asyncio
asyncio.run(main())