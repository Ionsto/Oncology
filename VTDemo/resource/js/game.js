//Game files world cell functions etc
var DEBUG = false;
function CellType()
{
	this.RadLim = 0;
	this.Id = 0;
	this.Name = "";
	this.Col = 1;
}
function Group(x,y)// one part of the person
{
	this.X = x;
	this.Y = y;
	this.Rad = 0;
	this.Type = 0;
}
function RadEmitter(x,y)
{
	this.SX = x;//mid point of circle
	this.SY = y;
	this.Rad = 10;
	this.X = Rad;
	this.Y = 0;
	this.Angle = 0;
	this.UpdatePos = function(Mx,My)
	{
		var theta = Math.atan2f(My - this.SY,Mx - this.SX);
		this.X = Rad * Math.cos(theta);
		this.Y = Rad * Math.sin(theta);
		return;
	};
}
function World(Xw,Yw)
{
	this.ColourArr = ["#FFFFFF","#FFFFAA","#FFFF00","#FF0000","#00FF00","#0000FF"];
	this.Rads = new Array(3);
	this.Rads[0] = new RadEmitter(Xw/2,Yw/2);
	this.SizeX = Xw;
	this.SizeY = Yw;
	this.Clear = true;
	this.CellCount = Xw * Yw;
	this.Types = new Array();
	this.Cells = new Array(this.CellCount);
	this.CellRender = new Array(this.CellCount);
	for(var i = 0;i< this.CellCount;++i)
	{
		this.Cells[i] = new Group(50,50);
		this.CellRender[i] = true;
	}
	if(DEBUG){console.log("built group");}
	this.Update = function(){

	};
}