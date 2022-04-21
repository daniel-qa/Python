# pip install retry
from retry import retry

@retry()
def make_trouble():
    '''Retry until succeed'''
    
    
@retry(ZeroDivisionError, tries=3, delay=2)
def make_trouble():
    '''Retry on ZeroDivisionError, raise error after 3 attempts, sleep 2 seconds between attempts.'''    
