# -*- coding: utf8 -*-
from retry import retry

''' 重試3次，間隔2秒 '''
@retry(ZeroDivisionError, tries=3, delay=2)
def make_trouble():
	'''Retry on ZeroDivisionError, raise error after 3 attempts, sleep 2 seconds between attempts.'''
	1/0
	print("hello")

try:
	#1/0
	make_trouble()
except Exception as e:
	print(e)

