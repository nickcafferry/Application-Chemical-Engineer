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


var ctx2 = document.getElementById("pie-chart2").getContext('2d');
var targetChart = new Chart(ctx2, {

	type: 'doughnut',
	data: {
		labels: fullname,
		datasets: dataChart
	},
	options: options
});
