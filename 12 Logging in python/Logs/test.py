from logger import logging

def add(a,b):

    logging.debug('The addition operation is taking place')
    return f'Addition: {a+b}'

logging.debug('The addition function is called.')
add(2,3)
