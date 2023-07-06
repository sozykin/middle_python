import logging

# Настройка логгера
logging.basicConfig(filename='my_app.log', 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Возникло исключение", exc_info=True)
    # logging.exception("Возникло исключение")