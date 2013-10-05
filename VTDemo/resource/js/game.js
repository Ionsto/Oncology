//Game files world cell functions etc

function Group(X,Y)// one part of the person
{
	this.X = x;
	this.Y = y;
}
function World()
{
	this.CellCount = 50;
	this.Cells = new Array(50);
	for(var i = 0;i< this.CellCount)
	{
		this.Cells = new Group();
	}
	this.Gen = function()
	{
		
	};
};