f = open('C:/Users/mpfs/Contacts/Documents/GitHub/Oncology/Model_View/workfile.txt', 'r')
while True:
	strs = f.readline()
	if(strs == ""):
		break
	else:
		strsS = strs.split(",")
		if(strsS[0] == "Herro"):
			int(print(strsS[1]))
			int(print(strsS[2]))
			int(print(strsS[3]))
f.close()