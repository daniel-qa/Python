from __future__ import division # 不管什麼情況，都是得到浮點數的結果。
import os,sys 
from time import sleep
import pyautogui
import logging
import pyperclip as pc


if __name__== "__main__":   
	print("This is main function called")
	
	l1 = [1, 1]
	l2 = [4, 3]
	
	l3 = [a / b for a, b in zip(l1, l2)] # 數值相除 
	print(l3) 
  
  ```
  Output
  [0.25,0.3333...]
  ```
  
