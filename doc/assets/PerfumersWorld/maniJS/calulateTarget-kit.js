
//console.log("calulate Target");
//console.log("quantity"+target);
//var tar = 0;
var cal = [];

var minus = 0;
var targetMax = 0
//Condition2 calculate finding How many Materials should be have from target%
for(var i = 0; i < target.length; i++) {
	var s = target[i];
//	var limit = target[i]/100*1;
//	console.log(limit);




	//	console.log(alpha[i]+":"+s);
	//	console.log(target[i]);
	//	console.log(targetMax);
		cal.push({
        "alpha": alpha[i],
        "cal": parseFloat(s),
				"indexof": i,
				"target":target[i]
    });
}

//Condition3 Sort Max to Min
cal.sort((a, b) => (b.cal > a.cal) ? 1 : -1);
//console.log(cal)
