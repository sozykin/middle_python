import time


def func1(x):
    print(x**2)
    time.sleep(3)
    print('func1 завершена')


def func2(x):
    print(x**0.5)
    time.sleep(3)
    print('func2 завершена')


def main():
    func1(4)
    func2(4)



start = time.time()

main()

print("Время выполнения, с: ", time.time() - start)

# print(type(func1))

# print(type(func1(4)))