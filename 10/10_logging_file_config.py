import logging
import logging.config

# Загружаем конфигурацию логгера
logging.config.fileConfig(fname='10/logger.conf', disable_existing_loggers=False)

# Получаем логгер, указанный в конфигурационном файле
logger = logging.getLogger('sampleLogger')

logger.debug('Это сообщение отладки (debug)')
logger.info('Это информационное сообщение (info)')
logger.warning('Это предупреждение (warning)')
logger.error('Это сообщение об ошибке (error)')
logger.critical('Это сообщение о критической ошибке (critical)')