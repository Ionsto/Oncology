//JSC3D.console.setup('debug', '120px');
var canvas = document.getElementById('renderframe');
var viewer = new JSC3D.Viewer(canvas);
var RotationX = 0;//abs rot
var RotationY = -90;//abs rot
var RotationZ = -90;//abs rot
viewer.setParameter('InitRotationX', 0);
viewer.setParameter('InitRotationY', -90);
viewer.setParameter('InitRotationZ', 90);
viewer.setParameter('ModelColor', '#AAAAFF');
viewer.setParameter('BackgroundColor1', '#FFFFFF');
viewer.setParameter('BackgroundColor2', '#FFFFFF');
viewer.setParameter('RenderMode', 'smooth');
viewer.setParameter('Definition','High');
viewer.setParameter('MipMapping', 'on');
viewer.enableDefaultInputHandler(false);
viewer.init();
viewer.update();
var md2_player = new JSC3D.Md2Player(viewer);
var PlaySpeedS = 1;
var loc = document.getElementById("loc");
var PlaySpeed = document.getElementById("Play");
var OutView = document.getElementById("veiwloc");
PlaySpeed.value = 0;
var Begining = "Looking from the front ";
var FPS = 0;
OutView.innerHTML = Begining + "at " + FPS.toString() + " days per second";//FPS System
//Rotate();
function SpeedChange()
{
	md2_player.pause();
	FPS = parseInt(PlaySpeed.value) / 10;//10 frames per day
	if(parseInt(PlaySpeed.value) != 0)
	{
		md2_player.play(parseInt(PlaySpeed.value));
	}
	OutView.innerHTML = Begining + "at " + FPS.toString() + " days per second";//FPS System
}
md2_player.replaceSceneFromUrls('resource/models/First/Data.md2', 'undefined', 'undefined', 'undefined');
function RotateView(x,y,z)
{
	viewer.rotate(x,y,z);
	RotationX += x;
	RotationY += y;
	RotationZ += z;
}
function Set()
{
	SetZero();
	RotateView(0, -90, 90);
	if (document.getElementById("0").checked) {//Front
		RotateView(0, 0, 0);
		Begining = "Looking from the front ";
	}
	if (document.getElementById("1").checked) {//Back
		RotateView(0, 180, 0);
		Begining = "Looking from the back ";
	}
	if (document.getElementById("2").checked) {//Left
		RotateView(0, 90, 0);
		Begining = "Looking from the left of the rectum ";
	}
	if (document.getElementById("3").checked) {//Right
		RotateView(0, -90, 0);
		Begining = "Looking from the right of the rectum ";
	}
	if (document.getElementById("4").checked) {//Odd rot
		RotateView(0, 45, 0);
		RotateView(30, 0, 0);
		Begining = "Looking from an oblique angle ";
	}
	OutView.innerHTML = Begining + "at " + FPS.toString() + " days per second";//FPS System
}
function SetZero()
{
	viewer.rotMatrix.identity();
	RotationX = 0;
	RotationY = 0;
	RotationZ = 0;
}