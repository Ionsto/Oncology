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
			if strsS[1] == "loc":
				ob.location.x = int(strsS[2])
				ob.location.y = int(strsS[3])
				ob.location.z = int(strsS[4])
			if strsS[1] == "sca":
				ob.scale.x = int(strsS[2])
				ob.scale.y = int(strsS[3])
				ob.scale.z = int(strsS[4])
f.close()