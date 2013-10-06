//Game files world cell functions etc
var DEBUG = false;

function Group(x,y)// one part of the person
{
	this.X = x;
	this.Y = y;
}
function World()
{
	this.CellCount = 50;
	this.Cells = new Array(50);
	for(var i = 0;i< this.CellCount;++i)
	{
		this.Cells = new Group();
	}
	if(DEBUG){console.log("built group");}
	this.Update = function()
	{
	};
}