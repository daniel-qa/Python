# -*- coding: utf8 -*-
from retry import retry

''' 重試3次，間隔2秒 '''
@retry(Exception, tries=3, delay=2)
def make_trouble():
        '''Retry on ZeroDivisionError, raise error after 3 attempts, sleep 2 seconds between attempts.'''
        print("hello")

        #1/0
        raise BaseException("= 自定義錯誤 =")
        print("Success")

try:
        #1/0
        make_trouble()
except Exception as e:
        print(e)
