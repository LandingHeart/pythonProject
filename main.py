import os
path = "/Users/shinan/Desktop/pythonTu"
arr = os.listdir(path)

for file in arr:
	print file 

newlist = [newlist[0] for newlist in arr]
print newlist

def removeDub(dubChar):
	final_list = []
	for char in dubChar:

		if char not in final_list:
			arr.append("dub")
			final_list.append(char)
	return final_list

def appendDub(dub):
	for dubC in dub:
		if dubC not in dub:
			arr.append("dub")
	return 
dubStr = removeDub(newlist)



