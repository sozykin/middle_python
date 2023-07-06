import logging

# Создаем custom logger
logger = logging.getLogger(__name__)

# Создаем handler'ы
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('custome_file.log', encoding='UTF-8')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Создаем форматтеры и добавляем их к handler'ам
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Добавляем handler'ы к logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.debug('Это сообщение отладки (debug)')
logger.info('Это информационное сообщение (info)')
logger.warning('Это предупреждение (warning)')
logger.error('Это сообщение об ошибке (error)')
logger.critical('Это сообщение о критической ошибке (critical)')