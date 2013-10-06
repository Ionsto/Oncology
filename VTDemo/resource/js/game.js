//Game files world cell functions etc
var DEBUG = false;

function Group(x,y)// one part of the person
{
	this.X = x;
	this.Y = y;
}
function World()
{
	this.Clear = true;
	this.CellCount = 50;
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