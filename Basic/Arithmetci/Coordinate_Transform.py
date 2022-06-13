from __future__ import division # 不管什麼情況，都是得到浮點數的結果。
import os,sys

FORMAT = '%(asctime)s %(message)s'            # 加入時間記錄
logging.basicConfig(level=logging.INFO,format=FORMAT)	# 關閉輸出

# 座標轉換
def Coordinate_Translate(x,y):

	Coordinate = [ 192, 16 ] 
	
	#Coordinate = [ x, y ] 
		
	Screen_Size = [ 1920, 1600 ]  # 1920 x 1600	
	
	# 先轉為百分比
	l1 = Coordinate
	l2 = Screen_Size 
	l3 = [ a / b for a,b in zip(l1,l2)]	
	print(l3)
	
	# 再轉為實際座標
	l4 = Screen_Size 
	l5 = [ a * b for a,b in zip(l3,l4)]	
	print(l5)
	
if __name__== "__main__":   
	print("This is main function called")

  # 座標轉換
	Coordinate_Translate(1,2)
	
