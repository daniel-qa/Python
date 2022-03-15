import os,sys
from time import sleep
import pyautogui
import logging
import pyperclip as pc

FORMAT = '%(asctime)s %(message)s'            # 加入時間記錄
logging.basicConfig(level=logging.INFO,format=FORMAT)	# 關閉輸出

# 上傳音樂檔
def Upload_Music():
	# 484 , 554
	logging.info("點擊音樂ICON")
	pyautogui.moveTo( 484 , 554 ) # Move the mouse to XY coordinates.
	pyautogui.click()
	
	## 628 , 640
	logging.info("點擊上傳ICON")
	pyautogui.moveTo( 628 , 640)   #上傳
	pyautogui.click()

	# 275, 796
	logging.info("點擊檔案PATH")
	pyautogui.moveTo( 275, 796)   # 檔案名稱
	pyautogui.click()
	sleep(1)
	#Switch_ENG_Keyboard()
	logging.info("輸入檔案路徑")
	
	music_file = "D:\daniel\Music\背景音樂\simple.mp3"
	pc.copy(music_file)
	
	# Pressing Ctrl+V
	logging.info("貼上檔案路徑")
	pyautogui.hotkey('ctrl', 'v')
	
	# 829 , 819
	logging.info("點擊上傳ICON")
	pyautogui.moveTo( 829 , 819)   # 開啟
	pyautogui.click()
	
if __name__== "__main__":   
    print("This is main function called")
    
    # 上傳音樂檔
    Upload_Music()
