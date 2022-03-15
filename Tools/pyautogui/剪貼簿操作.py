# 在 Python 中使用 pyperclip 模組將文字複製到剪貼簿
# pyperclip 模組用於在 Python 中實現跨平臺複製和貼上。它是一個跨平臺的庫，可用於不同的作業系統。此外，跨平臺複製貼上在 Python 中早先是不存在的。

# pyperclip 模組提供了 copy() 和 paste() 函式來幫助文字從剪貼簿流入和流出。pyperclip 模組可以通過使用 pip 命令簡單地安裝。
#pip install pyperclip


#以下程式碼使用 pyperclip 模組在 Python 中將文字複製到剪貼簿。

import pyperclip as pc
a1 = "Hey, nice to see you"
pc.copy(a1)
a2 = pc.paste()
print(a2)
print(type(a2))
# 輸出：
#
#Hey, nice to see you
#<class 'str'>
# 來自 pyperclip 模組的 copy() 和 paste() 函式都在這裡起作用。pyperclip 將遇到的每種資料型別轉換為字串。
