import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'D:\screenshot_1.png')

# 取得時間
from datetime import datetime
dt = datetime.now().strftime("%m-%d %H%M")
print(dt)

myScreenshot = pyautogui.screenshot()
myScreenshot.save('D:\\'+ dt +' screenshot_1.png')


# 設定 region
im = pyautogui.screenshot(region=(0,0, 300, 400))   # 左上，右下
