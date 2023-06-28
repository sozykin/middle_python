import asyncio
import time


async def func1(x):
    print(x**2)
    await time.sleep(3)
    print('func1 завершена')


async def func2(x):
    print(x**0.5)
    await time.sleep(3)
    print('func2 завершена')


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    await task1
    await task2

start = time.time()

asyncio.run(main())

print("Время выполнения, с: ", time.time() - start)

# print(type(func1))

# print(type(func1(4)))