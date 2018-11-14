import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from matplotlib import cm
import pandas
df = pandas.read_excel("data.xls")
groupeddays = df.groupby('Day number (1-37)')
CompiledData = []
MaxSliceCount = len(groupeddays)
DayCount = len(groupeddays)
for index,slices in groupeddays:
    data = pandas.DataFrame(slices).reset_index(drop=True)
    #print(data.count().max())
    CompiledData.append([])
    for dayindex,d in data.iterrows():
        #print(d.tolist())
        day,a,p,r,l = d.tolist()
        Center = ((a + p) / 2,(r + l) / 2,dayindex)
        Dimensions = (abs(a - p) / 2,abs(r - l))
        CompiledData[-1].append({"Center":Center,"Dimensions":Dimensions})
    for extra in range(MaxSliceCount - (dayindex+1)):
        CompiledData[-1].append({"Center":Center,"Dimensions":Dimensions})
def MakeEl(cent,dim,steps = 20):
    x = np.zeros(steps)
    y = np.zeros(steps)
    z = np.ones(steps) * cent[2] * 0.5
    for i,t in enumerate(np.linspace(0,2*np.pi,steps)):
        x[i] = cent[0] + dim[0]*np.cos(t)
        y[i] = cent[1] + dim[1]*np.sin(t)
    return x,y,z
Steps = 20
X = np.zeros((DayCount,MaxSliceCount,Steps))
Y = np.zeros((DayCount,MaxSliceCount,Steps))
Z = np.zeros((DayCount,MaxSliceCount,Steps))
for d,day in enumerate(CompiledData):
    for s,Circle in enumerate(day):
        Xm,Ym,Zm = MakeEl(Circle["Center"],Circle["Dimensions"],Steps)
        X[d,s] = Xm - day[0]["Center"][0]
        Y[d,s] = Ym - day[0]["Center"][1]
        Z[d,s] = Zm
Time = np.arange(0,DayCount)
InterpSteps = 20
InterpCount = DayCount * InterpSteps
InterpPoints = np.linspace(0,DayCount,InterpCount,endpoint=False)
XInterp = np.zeros((InterpCount,MaxSliceCount,Steps))
YInterp = np.zeros((InterpCount,MaxSliceCount,Steps))
ZInterp = np.zeros((InterpCount,MaxSliceCount,Steps))
for i in range(MaxSliceCount):
    for j in range(Steps):
        XInterp[:,i,j] = np.interp(InterpPoints,Time,X[:,i,j])
        YInterp[:,i,j] = np.interp(InterpPoints,Time,Y[:,i,j])
        ZInterp[:,i,j] = np.interp(InterpPoints,Time,Z[:,i,j])
        
# images = []
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.set_axis_off()
# for X,Y,Z in [(XInterp[i,:,:],YInterp[i,:,:],ZInterp[i,:,:]) for i in range(InterpCount)]:
#    images.append([ax.plot_wireframe(X, Y, Z)])
# ani = animation.ArtistAnimation(fig, images, interval=100, blit=True)
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, bitrate=1800,extra_args=["-y"])
# print("Save")
# ani.save('im.mp4',writer=writer)
# print("Finished")
print("Start")
fig = plt.figure()
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, bitrate=1800,extra_args=["-y"])
with writer.saving(fig, "other.mp4", InterpCount):
    for X,Y,Z,i in [(XInterp[i,:,:],YInterp[i,:,:],ZInterp[i,:,:],i) for i in range(InterpCount)]:
        print(i,InterpCount)
        time = "t = {}".format(int(np.floor(i/float(InterpSteps))))
        ax = fig.add_subplot(111, projection='3d')
        plt.xlim(-50,50)
        plt.ylim(-50,50)
        ax.set_aspect("equal")
        fig.text(0.1,0.1,time, fontsize=12)
        #ax.set_axis_off()
        ax.plot_surface(X, Y, Z)
        for s in range(MaxSliceCount):
            ax.plot(X[s], Y[s], Z[s],c="b")
        #plt.show()
        writer.grab_frame()
        fig.clf()
print("done")
#plt.show()
#Writer = animation.writers['ffmpeg']
#FFwriter = animation.FFMpegWriter()
#writer = Writer(fps=10, bitrate=1800,extra_args=["-y"])
#print("Save")
#ani.save('im.mp4',writer=writer)
#print("Done?")
# readings = df.groupb('Day number (1-37)')
# for day in (pandas.DataFrame(day[1]) for day in readings):
#     for i,cut in ((c[0],pandas.DataFrame(c[1])) for c in day.iterrows()):
#         print(i,cut["A"])
    #print(A)