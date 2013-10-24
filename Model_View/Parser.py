f = open('workfile.txt', 'r')
while True:
	strs = f.readline()
	if(strs == ""):
		break
	else:
		print(strs)
f.close()