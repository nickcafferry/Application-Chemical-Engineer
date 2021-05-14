//Remark9 convert object value on row to keys
	var keys = Object.values(row);

//Remark10 Create array addarr empty
	var addarr = {
    data: []
};
var icount = 0;
var totalsum = 0;
//var totalsum2 = 0;
var totallife = 0;
//console.log(target);
//Condition4 take each cal form Condition3
$.each(target, function(key, value){


	var alphachoose = value.alpha;
	var qtn = parseFloat(value);
	//var alphachoose = value.alpha;
	//var target = value.target;
	//keys.sort(compare);
	//console.log(keys.abcs[5]);
	//var maxVotes = 0;
	//var obj = [];
	var indexarr = key;
	var checkAbcs = '';

	//Condition5 take keys array by each (Materials query on Condition1) check case PointClass
	keys.map(function(val, index){

		//Remark11 get % on abcs fields on 0-25 by each index
		//console.log(qtn+" "+alphachoose);
		var valueMat = val.abcs[indexarr];
		var impactMat = val.Impact;
		var PointClass = 0;
		var classMat = parseFloat(valueMat);
		//keys[index]["PointClass"] = parseInt(PointClass);

		//Materials Name
		var nameMat = val.name;
	/*		console.log(nameMat);
			console.log(index);
		console.log(qtn);*/
		//console.log("Cal"+indexarr+"Val"+impactMat);
		//	PointClass = value;

				if (qtn == 0 && classMat == 0){
						PointClass = 0;
						keys[index]["PointClass2"].push(PointClass);
				//			console.log("case0 "+PointClass);
					}

				else if (qtn == classMat){
					PointClass = parseFloat(classMat);
					keys[index]["PointClass2"].push(PointClass);
			//	console.log("case1 "+PointClass);
				//	keys[index]["PointClass"] = parseInt(PointClass)+PointClass2;

				}

				else if (qtn == 0 && classMat > 0 ){
					PointClass = 0;
					keys[index]["PointClass2"].push(PointClass);
				//	console.log("case3 "+PointClass);
					//		keys[index]["PointClass"] = parseInt(PointClass)+PointClass2;

				}

				//   If Uni.Class(k) > Tv1(k) And Tv1(k) > 0 And Uni.Class(k) < 100 Then        'Case 6
				else if (qtn < classMat && classMat > 0){

					PointClass = parseFloat(qtn);
					keys[index]["PointClass2"].push(PointClass);

				//	console.log(PointClass+" case4");
					//			keys[index]["PointClass"] = parseInt(PointClass)+PointClass2;

				}
				//   If Uni.Class(k) > Tv1(k) And Tv1(k) > 0 And Uni.Class(k) < 100 Then        'Case 6
				else if (qtn > classMat && classMat > 0){

					PointClass = parseFloat(classMat);
					keys[index]["PointClass2"].push(PointClass);

				//	console.log(PointClass+" case5");
					//			keys[index]["PointClass"] = parseInt(PointClass)+PointClass2;

				}
				else if (classMat == 0 && qtn > classMat){

					PointClass = parseFloat(classMat);
					keys[index]["PointClass2"].push(PointClass);

				//	console.log(PointClass+" case5");
					//			keys[index]["PointClass"] = parseInt(PointClass)+PointClass2;

				}


				//		console.log("PointClass2"+PointClass2);

			//	console.log(keys[index].name);
		//		console.log(keys[index].abcs);
			//	console.log(keys[index].PointClass2);
			//Remark13 sum pointClass2 to Pointsum array object Keys
				keys[index]["Pointsum"] = sum(keys[index].PointClass2);

		//		console.log("Pointsum"+keys[index]["Pointsum"]);
			//	console.log("##################");
				//	PointClass2 = keys[index].PointClass;

			})
});
			//	console.log("point Sum");
			 	// console.log(keys);
				// console.log(keys["abcs"]);
			//	 console.log(keys.Pointsum);
				 keys = keys.filter(it => it.Pointsum > 1);

			//	 	 console.log(keys);
