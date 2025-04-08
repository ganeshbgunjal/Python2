import logging
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H-%M-%S',
    handlers= [
        logging.FileHandler('app1.log'),     #will save file logs
        logging.StreamHandler()                #will save streaming logs
    ]
)

logger = logging.getLogger('ArithmaticApp')

def add(a,b):
    result = a+b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result

def substract(a,b):
    result = a-b
    logger.debug(f'Substracting {a} - {b} = {result}')
    return result

def multiplication(a,b):
    result = a*b
    logger.debug(f'Multiplying {a} * {b} = {result}')
    return result

def division(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero error.')
        return None

add(10,15)
substract(15,10)
multiplication(10,20)
division(20,0)
