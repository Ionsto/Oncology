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
Step = 6
XOffset = -12
a = 0
p = 0
r = 0
l = 0
scales = 5
print("start")
def Set(ob):
	ob.location.x = (((a + p)/ 2) / scales) + XOffset
	ob.location.z = (slice * Step) / scales
	ob.location.y = ((r + l)/ 2) / scales
	ob.keyframe_insert(data_path='location', frame=(framec))
	ob.scale.x = ((abs(l - r) / 2) / scales) + 1
	ob.scale.y = ((abs(l - r) / 2) / scales) + 1
	ob.scale.z = 1
	ob.keyframe_insert(data_path='scale', frame=(framec))

for rx in range(1,sh.nrows):#go through each row and do something in blender
	if int(sh.cell_value(rx,0)) != day:
		day = int(sh.cell_value(rx, 0))
		#set none data points to upper slice
		for i in range(slice,15):
			Set(bpy.data.objects[GetName(i)])
		bpy.data.objects["Plane"].keyframe_insert(data_path='scale', frame=(framec))
		slice = 0
		framec += 10
	ob = bpy.data.objects[GetName(slice)]
	print(str(rx))
	#get a,p,l,r
	a = int(sh.cell_value(rx,1))
	p = int(sh.cell_value(rx,2))
	r = int(sh.cell_value(rx,3))
	l = int(sh.cell_value(rx,4))
	Set(ob)
	slice += 1