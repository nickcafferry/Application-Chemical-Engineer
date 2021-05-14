//var max = Math.max(parseInt(value));
var namlabel = ['aliFATic',
'iceBerg',
'Citrus',
'Dairy',
'Edible',
'Fruit',
'Green',
'Herb',
'Iris',
'Jasmin',
'Konifer',
'Linalool',
'Muguet',
'Narcotic',
'Orchid',
'Phenol',
'Balsam',
'Rose',
'Spice',
'Smoke',
'Animal',
'Vanilla',
'Wood',
'Musk',
'Earthy',
'Zolvent'
];
//console.log(value);
var arr= [];
var max = 0;
valuename.forEach(myFunction);

//console.log(valuename);
function myFunction(item, index) {

	if (parseFloat(item) >= max) {
     max = item;
   }
//console.log(max);

	 valuename.sort(function(a, b){return b - a});
	 //document.getElementById("demo").innerHTML = valuename[0]+" "+valuename[1];

	 arr += value.indexOf(valuename[index]);

}
var valuename = valuename.filter(isPositive);
function isPositive(value) {
  return value > 0;
}
var max1;var max2;var max3;var max4;var max5;var max6;var max7;var max8;var max9;var max10;var max11;var max12;var max13;var max14;var max15;var max16;var max17;var max18;var max19 = null;var max20;var max21;var max22;var max23;var max24;var max25;var max26= null;
//console.log(valuename);
max1 = createvalue.indexOf(valuename[0]);
createvalue.splice(max1, 1,999);
max2 = createvalue.indexOf(valuename[1]);
createvalue.splice(max2, 1,999);
max3 = createvalue.indexOf(valuename[2]);
createvalue.splice(max3, 1,999);
max4 = createvalue.indexOf(valuename[3]);
createvalue.splice(max4, 1, 999);
max5 = createvalue.indexOf(valuename[4]);
createvalue.splice(max5, 1, 999);
max6 = createvalue.indexOf(valuename[5]);
createvalue.splice(max6, 1, 999);
max7 = createvalue.indexOf(valuename[6]);
createvalue.splice(max7, 1, 999);
max8 = createvalue.indexOf(valuename[7]);
createvalue.splice(max8, 1, 999);
max9 = createvalue.indexOf(valuename[8]);
createvalue.splice(max9, 1, 999);
max10 = createvalue.indexOf(valuename[9]);
createvalue.splice(max10, 1, 999);
max11 = createvalue.indexOf(valuename[10]);
createvalue.splice(max11, 1, 999);
max12 = createvalue.indexOf(valuename[11]);
createvalue.splice(max12, 1, 999);
max13 = createvalue.indexOf(valuename[12]);
createvalue.splice(max13, 1, 999);
max14 = createvalue.indexOf(valuename[13]);
createvalue.splice(max14, 1, 999);
max15 = createvalue.indexOf(valuename[14]);
createvalue.splice(max15, 1, 999);
max16 = createvalue.indexOf(valuename[15]);
createvalue.splice(max16, 1, 999);
max17 = createvalue.indexOf(valuename[16]);
createvalue.splice(max17, 1, 999);
max18 = createvalue.indexOf(valuename[17]);
createvalue.splice(max18, 1, 999);
max19 = createvalue.indexOf(valuename[18]);
createvalue.splice(max19, 1, 999);
max20 = createvalue.indexOf(valuename[19]);
createvalue.splice(max20, 1, 999);
max21 = createvalue.indexOf(valuename[20]);
createvalue.splice(max21, 1, 999);
max22 = createvalue.indexOf(valuename[21]);
createvalue.splice(max22, 1, 999);
max23 = createvalue.indexOf(valuename[22]);
createvalue.splice(max23, 1, 999);
max24 = createvalue.indexOf(valuename[23]);
createvalue.splice(max24, 1, 999);
max25 = createvalue.indexOf(valuename[24]);
createvalue.splice(max25, 1, 999);
max26 = createvalue.indexOf(valuename[25]);
createvalue.splice(max26, 1, 999);

//document.getElementById("demo").innerHTML += index + ":" + parseInt(item)+ "<br>";

console.log(max3);
//alpha[max1]+alpha[max2]+alpha[max3]+alpha[max4]+alpha[max5]+alpha[max6]+alpha[max7]+alpha[max8]+alpha[max9]+alpha[max10]+alpha[max11]+alpha[max12]+alpha[max13]+alpha[max14]+alpha[max15]+alpha[max16]+alpha[max17]+alpha[max18]+alpha[max19]+alpha[max20]+alpha[max21]+alpha[max22]+alpha[max23]+alpha[max24]+alpha[max25]+alpha[max26];
var checkmax3; var checkmax4; var checkmax5; var checkmax6; var checkmax7; var checkmax8; var checkmax9; var checkmax10; var checkmax11; var checkmax12; var checkmax13; var checkmax14;
if (alpha[max3] == undefined){
	checkmax3 = '';
} else { checkmax3 = alpha[max3]; }
if (alpha[max4] == undefined){
	checkmax4 = '';
} else { checkmax4 = alpha[max4]; }
if (alpha[max5] == undefined){
	checkmax5 = '';
} else { checkmax5 = alpha[max5]; }
if (alpha[max6] == undefined){
	checkmax6 = '';
} else { checkmax6 = alpha[max6]; }
if (alpha[max7] == undefined){
	checkmax7 = '';
} else { checkmax7 = alpha[max7]; }
if (alpha[max8] == undefined){
	checkmax8 = '';
} else { checkmax8 = alpha[max8]; }
if (alpha[max9] == undefined){
	checkmax9 = '';
} else { checkmax9 = alpha[max9]; }
if (alpha[max10] == undefined){
	checkmax10 = '';
} else { checkmax10 = alpha[max10]; }
if (alpha[max11] == undefined){
	checkmax11 = '';
} else { checkmax11 = alpha[max11]; }
if (alpha[max12] == undefined){
	checkmax12 = '';
} else { checkmax12 = alpha[max12]; }
if (alpha[max13] == undefined){
	checkmax13 = '';
} else { checkmax13 = alpha[max13]; }
if (alpha[max14] == undefined){
	checkmax14 = '';
} else { checkmax14 = alpha[max14]; }


var PWref = alpha[max1]+alpha[max2]+checkmax3+checkmax4+checkmax5+checkmax6+checkmax7+checkmax8+checkmax9+checkmax10+checkmax11+checkmax12+checkmax13+checkmax14;
document.getElementById("FormulaName").value = namedes+" "+namlabel[max1]+" "+namlabel[max2];
document.getElementById("createname").value = namedes+" "+namlabel[max1]+" "+namlabel[max2];
document.getElementById("PWref").value = PWref;