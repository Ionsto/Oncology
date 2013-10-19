//Game files world cell functions etc
var DEBUG = false;
function CellType()
{
	this.RadLim = 0;
	this.Id = 0;
	this.Name = "";
	this.Col = 1;
	this.Weight = 5;//E.g. Spine has a high weight 
    //The weight is the amount LOST when death oucoures.
    //Cancer has a negitive weight
}
function Group(x,y)// one part of the person
{
	this.X = x;
	this.Y = y;
	this.Rad = 0;
	this.Type = 0;
}
function RadEmitter(x, y)
{
    this.SX = x * 20.0;//mid point of circle
    this.SY = y * 20.0;
	this.Rad = x * 20 + 60;
	this.X = this.Rad;
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
    if(DEBUG){console.log("world start");}
    if (DEBUG) { console.log("colour array init");} 
    this.ColourArr = ["#FFFFFF", "#FFFFAA", "#FFFF00", "#FF0000", "#00FF00", "#0000FF", "#00AAFF", "#505AFF", "#505AFF", "#505AFF", "#505AFF"];
    if (DEBUG) { console.log("Rad array init"); }
    this.Rads = new Array(3);
    this.RadsRender = new Array(3);
    this.RadsRender[0] = true;
    this.Rads[0] = new RadEmitter(Xw / 2, Yw / 2);
	if (DEBUG) { console.log("Size Def"); }
	this.SizeX = Xw;
	this.SizeY = Yw;
	this.Clear = true;
	this.CellCount = Xw * Yw;
	if (DEBUG) { console.log("Type / group def"); }
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
	    for (var i = 0; i < this.CellCount; ++i) {
	        //Logic
	        if (this.Cells[i].Rad > this.Types[this.Cells[i].Type].RadLim) {

	        }
	    }
	};
	this.Fire = function () {
	};
	this.Fitness = function () {

	};
}