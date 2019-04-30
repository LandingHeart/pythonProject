import os
path = "/Users/shinan/Desktop/TestingFolder"
arr = os.listdir(path)

for file in arr:
	print file 

newlist = [newlist[0] for newlist in arr]
print newlist