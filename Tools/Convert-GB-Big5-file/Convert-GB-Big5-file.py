import os
import sys
import chinese_converter

file1='zh-TW.js'
file2= 'zh-TW-Convert.js'

# Read File
f = open(file1)

text = f.read()
#print(text)
f.close


# Convert to BIG5

str2 = chinese_converter.to_traditional(text)


#print(str2)


# Write to file

path = file2
f = open(path, 'w')
f.write(str2)
f.close()


# Reading files, and Compare
f1 = open(file1, "r")
f2 = open(file2, "r")

i = 0

for line1 in f1:
	i += 1

	for line2 in f2:

		# matching line1 from both files
		if line1 == line2:
			# print IDENTICAL if similar
			#print("Line ", i, ": IDENTICAL")
			pass
		else:
			print("Line ", i, ":")
			# else print that line from both files
			print("\tFile 1:", line1, end='')
			print("\tFile 2:", line2, end='')
		break

# closing files
f1.close()
f2.close()
