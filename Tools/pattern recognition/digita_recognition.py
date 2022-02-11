'''
簡單的圖形數字辨識
'''
from PIL import Image
import pytesseract
  
img = Image.open('test1.png')
text = pytesseract.image_to_string(img, lang='eng')
print(text)



'''
1.要安裝 Tesseract 主程式

  https://github.com/UB-Mannheim/tesseract/wiki
  tesseract-ocr-w64-setup-v5.0.1.20220118.exe
  
2.要有TESSDATA_PREFIX 環境變數:

TESSDATA_PREFIX  C:\Program Files (x86)\Tesseract-OCR\tessdata

'''
