import bpy
import xlrd
def GetName(i):
	i = int(i)
	if len(str(i)) == 1:
		return "slice.00" + str(int(i))
	if len(str(i)) == 2:
		return "slice.0" + str(int(i))
	if len(str(i)) == 3:
		return "slice." + str(int(i))
	return "snope"
book = xlrd.open_workbook("data.xls")
sh = book.sheet_by_index(0)
day = 1
slice = 0
framec = 0
a = 0
p = 0
r = 0
l = 0
scales = 20
print("start")
for rx in range(1,sh.nrows):#go through each row and do something in blender
	if int(sh.cell_value(rx,0)) != day:
		day = int(sh.cell_value(rx, 0))
		for i in range(slice,15):
			ob = bpy.data.objects[GetName(i)]
			ob.location.x = ((a + p)/ 2) / scales
			ob.location.z = (slice * 0.5)
			ob.location.y = ((r + l)/ 2) / scales
			ob.keyframe_insert(data_path='location', frame=(framec))
		slice = 0
		framec += 10
	ob = bpy.data.objects[GetName(slice)]
	print(str(rx))
	a = int(sh.cell_value(rx,1))
	p = int(sh.cell_value(rx,2))
	r = int(sh.cell_value(rx,3))
	l = int(sh.cell_value(rx,4))
	ob.location.x = ((a + p)/ 2) / scales
	ob.location.z = (slice * 0.5)
	ob.location.y = ((r + l)/ 2) / scales
	ob.keyframe_insert(data_path='location', frame=(framec))
	slice += 1
	#ob.keyframe_insert('location', framec)
	#ob.keyframe_insert(data_path='scale', frame)
	#print sh.row(rx)
'''
#f = open('C:/Users/mpfs/Contacts/Documents/GitHub/Oncology/Model_View/workfile.txt', 'r')
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
'''