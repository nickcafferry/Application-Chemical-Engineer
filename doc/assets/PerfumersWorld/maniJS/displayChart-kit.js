
var valueChart = [];
var arraytext = "";
var text = "Quantity,Sku,Name,family,abcs,impact,Price,qtyGram,"+datetimeFor+"\n";
var myObj = addarr.data;
var totalsumObj = 0;
var totallifeObj = 0;
var totalA = 0;
var quntOL = 0;
var avgLife =0;
var adjustOL = 0;
var calChartlife = 0;
var nameSave = '';
var chartsuma = 0; var chartsumb = 0;var chartsumc = 0; var chartsumd = 0;var chartsume = 0;var chartsumf = 0;var chartsumg = 0;var chartsumh = 0;
var chartsumi = 0; var chartsumj = 0;var chartsumk = 0; var chartsuml = 0;var chartsumm = 0;var chartsumn = 0;var chartsumo = 0;var chartsump = 0;
var chartsumq = 0; var chartsumr = 0;var chartsums = 0; var chartsumt = 0;var chartsumu = 0;var chartsumv = 0;var chartsumw = 0;var chartsumx = 0;
var chartsumy = 0; var chartsumz = 0;
for ( var i in myObj) {
	var sku = myObj[i].sku;
	var name = myObj[i].name;
	var family = myObj[i].family;
	var abcs = myObj[i].abcs;
	var impact = myObj[i].impact;
	var price = myObj[i].price;
	var life = myObj[i].life;
	var percent = roundToTwo((myObj[i].calulate2) / totalsum * 100).toFixed(2);
	var percentGram = (percent/10).toFixed(2);
	var classa = myObj[i].ClassA*percent;
	var classb = myObj[i].ClassB*percent;
	var classc = myObj[i].ClassC*percent;
	var classd = myObj[i].ClassD*percent;
	var classe = myObj[i].ClassE*percent;
	var classf = myObj[i].ClassF*percent;
	var classg = myObj[i].ClassG*percent;
	var classh = myObj[i].ClassH*percent;
	var classi = myObj[i].ClassI*percent;
	var classj = myObj[i].ClassJ*percent;
	var classk = myObj[i].ClassK*percent;
	var classl = myObj[i].ClassL*percent;
	var classm = myObj[i].ClassM*percent;
	var classn = myObj[i].ClassN*percent;
	var classo = myObj[i].ClassO*percent;
	var classp = myObj[i].ClassP*percent;
	var classq = myObj[i].ClassQ*percent;
	var classr = myObj[i].ClassR*percent;
	var classs = myObj[i].ClassS*percent;
	var classt = myObj[i].ClassT*percent;
	var classu = myObj[i].ClassU*percent;
	var classv = myObj[i].ClassV*percent;
	var classw = myObj[i].ClassW*percent;
	var classx = myObj[i].ClassX*percent;
	var classy = myObj[i].ClassY*percent;
	var classz = myObj[i].ClassZ*percent;
	//100% push on TextFile
//	var percentbk = roundToTwo((myObj[i].calulate) / totalsum * 100).toFixed(2);


	totallifeObj += parseFloat(life);
	totalsumObj += parseFloat(percent);
	quntOL += parseFloat(percent)*parseFloat(life);
	avgLife = quntOL/totalsumObj;


/*calChartlife = percent*impact*((life-0)/life);

if (calChartlife < 1){
calChartlife = 0;
}
*/
if (i == 0){
	nameSave = email;
} else if (i == 1) {
	nameSave = valuefor;
} else {
	nameSave = '';
}
	text += percent+","+sku+","+name+",,,,"+price+","+percentGram+","+nameSave+"\n";

	arraytext += percent+","+sku+","+name+",,,,"+price+","+percentGram+"<br>";

	chartsuma += classa
	chartsumb += classb
	chartsumc += classc
	chartsumd += classd
	chartsume += classe
	chartsumf += classf
	chartsumg += classg
	chartsumh += classh
	chartsumi += classi
	chartsumj += classj;
	chartsumk += classk;
	chartsuml += classl;
	chartsumm += classm;
	chartsumn += classn;
	chartsumo += classo;
	chartsump += classp;
	chartsumq += classq;
	chartsumr += classr;
	chartsums += classs;
	chartsumt += classt;
	chartsumu += classu;
	chartsumv += classv;
	chartsumw += classw;
	chartsumx += classx;
	chartsumy += classy;
	chartsumz += classz;
}
$('#Ltotal').text((avgLife).toFixed(0));
//console.log("avgLife"+avgLife);
//valueHalflife.push(suma,sumb,sumc,sumd,sume,sumf,sumg,sumh,sumi,sumj,sumk,suml,summ,sumn,sumo,sump,sumq,sumr,sums,sumt,sumu,sumv,sumw,sumx,sumy,sumz);
valueChart.push(chartsuma,chartsumb,chartsumc,chartsumd,chartsume,chartsumf,chartsumg,chartsumh,chartsumi,chartsumj,chartsumk,chartsuml,chartsumm,chartsumn,chartsumo,chartsump,chartsumq,chartsumr,chartsums,chartsumt,chartsumu,chartsumv,chartsumw,chartsumx,chartsumy,chartsumz);

//document.getElementById("start").max = avgLife*5;


$('#gtotal').text((totalsumObj).toFixed(2));
//console.log(arraytext);
$('#textdes').val(arraytext);






var progress = document.getElementById('animationProgress');
//console.log(value);
//valueChart
var dataChart = [{
	data: value,
	labels: alpha,
	backgroundColor: color,
	borderColor: "#fff"
}];

var options = {
	tooltips: {
		enabled: true,
		mode: 'index',
	/*	callbacks: {
 			 title: function(tooltipItems, data) {
 				 return '';
 			 },
 			 label: function(tooltipItem, data) {
 				 var datasetLabel = '';
 				 var label = data.labels[tooltipItem.index];
 				 return label;
 				// return data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
 			 }
 		 },*/
	//	intersect: true,

	},
	legend: {
		display: false,
		labels: {
			fontColor: 'rgb(255, 99, 132)'
		}
	},
	animation: {
				duration: 1000,
				animation: true,
				animationSteps: 800,
				animationEasing:"easeInQuart", //"easeOutBounce",
				animateRotate: true,
				animateScale: true,
			/*	onProgress: function(animation) {
					progress.value = animation.currentStep / animation.numSteps;
				},
				onComplete: function() {
						progress.value = 100;
				/*	window.setTimeout(function() {
						progress.value = 0;
					}, 2000);*/
				//}
			},
	//percentageInnerCutout: 50, // This is 0 for Pie charts

	//Number - Amount of animation steps
	animationSteps: 800,

	//String - Animation easing effect
	animationEasing: "easeOutBounce",

	//Boolean - Whether we animate the rotation of the Doughnut
	animateRotate: true,

	//Boolean - Whether we animate scaling the Doughnut from the centre
	animateScale: true,
	plugins: {
		legend: {
			position: 'top',
		},
		datalabels: {

			formatter: (valueChart, ctx) => {

				var sum = 0;
				var dataArr = ctx.chart.data.datasets[0].data;
				var labell = ctx.chart.data.labels[ctx.dataIndex];
				var res = labell.split("-",1);
				//	let label = ctx.chart.data.datasets[0].labels;
				dataArr.map(data => {
					sum += parseInt(data);
				});

				var percentage = (valueChart*100 / sum).toFixed(0);
			//		console.log(res+" "+parseInt(percentage));
				return res+" "+parseInt(percentage);
			},
			display: function(context) {
			//	console.log(context.dataset.data);
				var dis = context.dataset.data[context.dataIndex] >= 1;

				return dis;// or >= 1 or ...

			},
			color: '#00000f',

		},
	}

};


/*var ctx = document.getElementById("pie-chart").getContext('2d');
var myChart = new Chart(ctx, {

	type: 'doughnut',
	data: {
		labels: fullname,
		datasets: dataChart
	},
	options: options
});*/
