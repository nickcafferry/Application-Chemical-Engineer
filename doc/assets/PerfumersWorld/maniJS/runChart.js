
	function manageCharts() {
		 // myChart.options.title.text = 'new title';
		 myChart.data.labels.pop();
		 myChart.data.datasets.forEach((dataset) => {
		 dataset.data.pop();

 });

	    myChart.update({duration: 0});
	}

//Half life Chart Automatically



//start animate Pie Charts
function DisplayChange(newvalue) {

	document.getElementById("value").innerHTML = newvalue;

	calChart(newvalue);

}


	var valuepush = [];
	//Sum Quantity/ Sum Life
	//var arrcheck = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];




//Start Half life
var timelapse = 0;
var suma = 0; var sumb = 0;var sumc = 0; var sumd = 0;var sume = 0;var sumf = 0;var sumg = 0;var sumh = 0;
var sumi = 0; var sumj = 0;var sumk = 0; var suml = 0;var summ = 0;var sumn = 0;var sumo = 0;var sump = 0;
var sumq = 0; var sumr = 0;var sums = 0; var sumt = 0;var sumu = 0;var sumv = 0;var sumw = 0;var sumx = 0;
var sumy = 0; var sumz = 0;
function calChart(newvalue) {
	timelapse = 0;
	var calde = 0;
	var valuesum = [];

	valuepush = [];
	suma = 0;  sumb = 0; sumc = 0;  sumd = 0; sume = 0; sumf = 0; sumg = 0; sumh = 0;
	sumi = 0;  sumj = 0; sumk = 0;  suml = 0; summ = 0; sumn = 0; sumo = 0; sump = 0;
	sumq = 0;  sumr = 0; sums = 0;  sumt = 0; sumu = 0; sumv = 0; sumw = 0; sumx = 0;
	sumy = 0;  sumz = 0;
	if (newvalue != ''){
		timelapse = newvalue;
		console.log(timelapse);
	}
	document.getElementById("value2").innerHTML = timelapse;
	for ( var i in myObj) {
		var sku = myObj[i].sku;
		var name = myObj[i].name;
		var family = myObj[i].family;
		var abcs = myObj[i].abcs;
		var impact = myObj[i].impact;
		var price = myObj[i].price;
		var life = myObj[i].life;
		 var classa = myObj[i].ClassA;
		 var classb = myObj[i].ClassB;
		 var classc = myObj[i].ClassC;
		 var classd = myObj[i].ClassD;
		 var classe = myObj[i].ClassE;
		 var classf = myObj[i].ClassF;
		 var classg = myObj[i].ClassG;
		 var classh = myObj[i].ClassH;
		 var classi = myObj[i].ClassI;
		 var classj = myObj[i].ClassJ;
		 var classk = myObj[i].ClassK;
		 var classl = myObj[i].ClassL;
		 var classm = myObj[i].ClassM;
		 var classn = myObj[i].ClassN;
		 var classo = myObj[i].ClassO;
		 var classp = myObj[i].ClassP;
		 var classq = myObj[i].ClassQ;
		 var classr = myObj[i].ClassR;
		 var classs = myObj[i].ClassS;
		 var classt = myObj[i].ClassT;
		 var classu = myObj[i].ClassU;
		 var classv = myObj[i].ClassV;
		 var classw = myObj[i].ClassW;
		 var classx = myObj[i].ClassX;
		 var classy = myObj[i].ClassY;
		 var classz = myObj[i].ClassZ;
		 var percent = roundToTwo((myObj[i].calulate2) / totalsum * 100).toFixed(2);

		 var calde = percent*impact*((life-timelapse)/life);


if (calde < 1){
	calde = 0;
}
//console.log(calde);
	suma += classa*calde;
	sumb += classb*calde;
	sumc += classc*calde;
	sumd += classd*calde;
	sume += classe*calde;
	sumf += classf*calde;
	sumg += classg*calde;
	sumh += classh*calde;
	sumi += classi*calde;
	sumj += classj*calde;
	sumk += classk*calde;
	suml += classl*calde;
	summ += classm*calde;
	sumn += classn*calde;
	sumo += classo*calde;
	sump += classp*calde;
	sumq += classq*calde;
	sumr += classr*calde;
	sums += classs*calde;
	sumt += classt*calde;
	sumu += classu*calde;
	sumv += classv*calde;
	sumw += classw*calde;
	sumx += classx*calde;
	sumy += classy*calde;
	sumz += classz*calde;

//console.log(name+"="+suma+" "+sumb+" "+sumc+" "+sumd+" "+sume+" "+sumf+" "+sumg+" "+sumh+" "+sumi+" "+sumj+" "+sumk+" "+suml+" "+summ+" "+sumn+" "+sumo+" "+sump+" "+sumq+" "+sumr+" "+sums+" "+sumt+" "+sumu+" "+sumv+" "+sumw+" "+sumx+" "+sumy+" "+sumz);

	//console.log("classw*calde "+(classw)+"*"+(calde));
	//console.log("sumw "+sumw);

	}
	valuepush.push(suma,sumb,sumc,sumd,sume,sumf,sumg,sumh,sumi,sumj,sumk,suml,summ,sumn,sumo,sump,sumq,sumr,sums,sumt,sumu,sumv,sumw,sumx,sumy,sumz);
	myChart.data.datasets[0].data = valuepush;
	//console.log(valuepush);
	myChart.update({duration: 1000});
	//return valuesum;
	//timelapse++;
//	console.log(timelapse);

}

var flag = true;
var interval;
var updateInterval = 150;
var addvalue = 1;
var g =0;

var c = 0;
var t;
var clabel = 0;
var timer_is_on = 0;
var stopLife = (avgLife).toFixed(0);
var timeinterval = 500;
function startCount() {
	//timelapse = 0;
	 $("#startbutton").hide();
	 $("#stopbutton").show();
  if (!timer_is_on) {
    timer_is_on = 1;

    timedCount();

  }

}

function stopCount() {
	$("#startbutton").show();
	$("#stopbutton").hide();
  clearTimeout(t);
  timer_is_on = 0;
	//document.getElementById("start").value = timer_is_on;
	//document.getElementById("value").innerHTML = timer_is_on;
//	timelapse = 0;

}
function timedCount() {
	timelapse = 0;


	calChart(c);
  c = c + 1;
	document.getElementById("start").value = clabel;

	document.getElementById("value").innerHTML = clabel;
	clabel = clabel +1;

	timeinterval = (timeinterval*((stopLife-(timelapse*0.1))/stopLife)).toFixed(2);
  t = setTimeout(timedCount, timeinterval);
  //console.log("timeinterval "+timeinterval);
	var allEqual =  valuepush => valuepush.every( v => v === valuepush[0] );

	//console.log(valuepush);
	var count = 0;
	for(var i = 0; i < valuepush.length; ++i){
		if(valuepush[i] > 0)
		count++;
	}
//console.log(count);

if (count <= 4){
	stopCount()
}

}
