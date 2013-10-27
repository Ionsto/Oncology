import bpy
f = open('C:/Users/mpfs/Contacts/Documents/GitHub/Oncology/Model_View/workfile.txt', 'r')
while True:
	strs = f.readline()
	if(strs == ""):
		break
	else:
		strsS = strs.split(",")
		if(strsS[0] == "slice"):
			me = bpy.data.meshes.new("mesh")
			ob = bpy.data.objects.new("slice", me)
			ob.location.x = int(strsS[1])
			ob.location.y = int(strsS[2])
			ob.location.z = int(strsS[3])
f.close()