'''
簡單的圖形數字辨識
'''
from PIL import Image
import pytesseract
  
img = Image.open('test1.png')
text = pytesseract.image_to_string(img, lang='eng')
print(text)
