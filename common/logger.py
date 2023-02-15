from loguru import logger


def get_logger(file):
    logger.add(sink=file, encoding='utf-8',
               # level='ERROR',
               # rotation='100 MB'
               )
    return logger


my_log = get_logger('cases.log')
