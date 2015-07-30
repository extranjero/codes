//Interface not exist on js thats why its implemented with TS

//Implementing interface with ducktyping
function printLabel(labelObj: {label:string}) {
	console.log(labelObj.label);
}

var obj = {size: 10, label: "Size 10 Object"};

printLabel(obj);

//Impelementing interface with interface

interface labelValue {
	label: string;
}

function printLabelI(labelObj: labelValue) {
	console.log(labelObj.label);
}

printLabelI(obj);

//Optional parametres
interface SquareConfig {
	color?: string; //fields with ? character are optional
	width: number;
}

function createSquare(config: SquareConfig): {color: string; area: number} {
	var newSquare = {color: "white", area:0};
	
	if(config.color){
		newSquare.color = config.color;
	}
	
	newSquare.area = config.width * config.width;	

	return newSquare;
}

var mySquare = createSquare({width: 5});
var mySquare2 = createSquare({width: 5, color:"red"});

console.log(mySquare, mySquare2);

//Interface functions

interface SearchFunc {
	(source: string, subString: string): boolean;
}

var mySearch: SearchFunc;

mySearch = function(src: string, sub: string){
	var result = src.search(sub);
	if(result == -1){
		return false;
	}

	return true;
}

console.log(mySearch("i have sub and more", "sub"));

