
//Condition6 each cal again to find max Pointsum on Materials
var nameMatarr = [];
var matchNameArr = [];
var checkName ='';
var valuesumTotal = [];
var textfile = '';
var lastqtn = 0;
var objsuma = 0; var objsumb = 0;var objsumc = 0; var objsumd = 0;var objsume = 0;var objsumf = 0;var objsumg = 0;var objsumh = 0;
var objsumi = 0; var objsumj = 0;var objsumk = 0; var objsuml = 0;var objsumm = 0;var objsumn = 0;var objsumo = 0;var objsump = 0;
var objsumq = 0; var objsumr = 0;var objsums = 0; var objsumt = 0;var objsumu = 0;var objsumv = 0;var objsumw = 0;var objsumx = 0;
var objsumy = 0; var objsumz = 0;
	 $.each(cal, function(key, value){
		var maxVotes = 0;
		var obj = [];
		var qtn = parseFloat(value.cal);
		var indexarr = value.indexof;
//			console.log(value);
//		console.log("position"+qtn);
		//keys.sort(compare);

		//var maxVotes = 0;
		//var obj = [];


		if (qtn > 0){
			 for (var h = 0; h <= keys.length; h++){

				 //check if indexarr of qtn = 0 delete keys
				// console.log(keys);
				 // Get the object having votes as max votes
				// var obj = games.find(game => game.votes === maxVotes);
				maxVotes = Math.max(...keys.map(e => e.abcs[indexarr]));
			//	 maxVotes = Math.max(...keys.map(e => e.Pointsum));
				// let maxGame = games.reduce((max, game) => max.votes > game.votes ? max : game);

	 		obj = keys.find(game => game.abcs[indexarr] === maxVotes);
				// obj = keys.find(game => game.Pointsum === maxVotes);



			//	 obj = obj2.find(game2 => game2.abcs[indexarr] === maxVotes2);
				 //const filteredItems = keys.slice(0, h).concat(keys.slice(h + 1, keys.length));
			 }

	/*		 for (var j = 0; j <= keys.length; j++){

				 //check if indexarr of qtn = 0 delete keys

				 maxVotes2 = Math.max(...keys.map(e => e.abcs[indexarr]));


				 obj = keys.find(game2 => game2.abcs[indexarr] === maxVotes2);

			 }*/
			// var objname = obj.name;

//Condition7 take Name of materials in list to calulate impact and classHr
if (obj == undefined|| obj == null) {
//	console.log("null");
//console.log(obj);
}
//row.splice(row.indexOf(obj.name), 1 );
else {
//	var i = array.indexOf(obj.name);

var splitName = obj.name.split(" ");

//console.log(obj.name);
if (nameMatarr.includes(splitName[0]) == false){
	nameMatarr.push(splitName[0]);
	matchNameArr.push(obj.name);
	var n = nameMatarr.indexOf(splitName[0]);
	var n2 = nameMatarr.indexOf(splitName[1]);
	//console.log(qtn);


}

if (n != -1 && n!=undefined) {


		checkName = obj.name;
	//	console.log(checkName);
	/*	console.log(splitName[0]);

	console.log(nameMatarr);
console.log(matchNameArr);*/
	var indexgg = keys.findIndex(findrow => findrow.name==checkName);





if(indexgg != -1) {
	keys.splice(indexgg, 1);
}
/*console.log(checkName);
console.log("qtn"+qtn);
//	var indexde = index;
console.log("maxVotes="+maxVotes);
//keys = row.splice(indexde,1);
console.log("------------------");*/
// keys.slice(1,n)

//addarr = addarr.push(obj)

if (obj.Impact == 0 ){
	obj.Impact = 100;
}
if (obj.ClassHr == 0) {
	obj.ClassHr = 1;
}
var res = obj.sku.substring(0, 1);

//console.log("count  "+icount);
var sumall = 0;
var jj = 0;
//console.log("icount"+icount);
if (icount < needmat){
//Condition calculate qtn * 100 / impact
//console.log("qtn = "+qtn);
	var calculate2 = parseFloat(qtn).toFixed(2);
//	console.log("calculate2 = "+calculate2);

	//nameobj = obj.name;
//	var calculate = parseFloat(calculate);
//	calculate2 = parseFloat(calculate2);
	/*if (res == 8){
		if (calculate > 0.5){
			calculate = calculate*0.02;
		}
	}*/
	var limitobj = obj.limitFra;
	var DoseFraMaxObj = obj.DoseFraMax;

	//	console.log("limitFra "+limitobj);
	//	console.log("DoseFraMaxObj "+DoseFraMaxObj);
		//Check calulate percent > DoseFraMax


//	console.log("calculate "+nameobj+": "+calculate2);

	if (calculate2 > 0.01) {
		totalsum += parseFloat(calculate2);
	//	totalsum2 += parseFloat(calculate2);
		totallife += parseInt(obj.ClassHr);

		textfile += checkName+"|"+target+ "|"+obj.abcs+'|'+obj.Pointsum+'|';
	//console.log(checkName);
		//Condition7.1 Push Materials object and Calculate(Percent%) value to addarr array(Remark10)
		addarr.data.push({
			"name": checkName,
			"sku": obj.sku,
			"family": obj.family_id,
			"abcs": obj.Class2,
			"price": obj.price,
			"qtn": qtn.toFixed(4),
			"impact": obj.Impact,
			"limitFra":obj.limitFra,
			"DoseFraMax":obj.DoseFraMax,
			"Pointsum": obj.Pointsum,
			"calulate2": calculate2,
		//	"calulate": calculate,
			"life": obj.ClassHr,
			"ClassA": parseFloat(obj.Class_1),
			"ClassB": parseFloat(obj.Class_2),
			"ClassC": parseFloat(obj.Class_3),
			"ClassD": parseFloat(obj.Class_4),
			"ClassE": parseFloat(obj.Class_5),
			"ClassF": parseFloat(obj.Class_6),
			"ClassG": parseFloat(obj.Class_7),
			"ClassH": parseFloat(obj.Class_8),
			"ClassI": parseFloat(obj.Class_9),
			"ClassJ": parseFloat(obj.Class_10),
			"ClassK": parseFloat(obj.Class_11),
			"ClassL": parseFloat(obj.Class_12),
			"ClassM": parseFloat(obj.Class_13),
			"ClassN": parseFloat(obj.Class_14),
			"ClassO": parseFloat(obj.Class_15),
			"ClassP": parseFloat(obj.Class_16),
			"ClassQ": parseFloat(obj.Class_17),
			"ClassR": parseFloat(obj.Class_18),
			"ClassS": parseFloat(obj.Class_19),
			"ClassT": parseFloat(obj.Class_20),
			"ClassU": parseFloat(obj.Class_21),
			"ClassV": parseFloat(obj.Class_22),
			"ClassW": parseFloat(obj.Class_23),
			"ClassX": parseFloat(obj.Class_24),
			"ClassY": parseFloat(obj.Class_25),
			"ClassZ": parseFloat(obj.Class_26),

		});



	}
	//console.log(icount);
	icount++;
}
}
else {
//console.log("else"+obj.name);
var indexgg = keys.findIndex(findrow => findrow.name==obj.name);
if(indexgg != -1) {
	keys.splice(indexgg, 1);
}
}

}
}

});


//console.log(addarr);
