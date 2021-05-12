


var valcheck;
			function updateValue() {
				var items = [];
				for (i=0; i<len; i++){

					var txt = alpha[i];
					var boxvalue = document.getElementById('myRange'+txt).value;
					items.push(boxvalue);

				}
			//	console.log(items);
				return items
				items.length = 0;
				items = [];

			}
		$.each(alpha , function (index, value){
			$(".pos"+value).click(function () {
							var oldValue = document.getElementById('myRange'+value).value;
							if (oldValue <= 99){
							var val = parseInt(oldValue) +1;
						} else {
							var val = parseInt(oldValue);
						}
						//	$('#theprogressbarA').attr('aria-valuenow', val).css('width', val+'%');
							var fn = 'progressbar'+value;

								$('#textvalue'+value).removeAttr("hidden");
							$('#myRange'+value).val(val);
							$('#textvalue2'+value).text(val);


							if(fn == 'progressbarA'){

							progressbarA(val);

						}
						if(fn == 'progressbarB'){
							progressbarB(val);
						//	console.log(fn);
						}
						if(fn == 'progressbarC'){
							progressbarC(val);
					//		console.log(fn);
						}
						if(fn == 'progressbarD'){
							progressbarD(val);
					//		console.log(fn);
						}
						if(fn == 'progressbarE'){
							progressbarE(val);
						//	console.log(fn);
						}
						if(fn == 'progressbarF'){
							progressbarF(val);
						//	console.log(fn);
						}	if(fn == 'progressbarG'){
							progressbarG(val);
						//	console.log(fn);
						}	if(fn == 'progressbarH'){
							progressbarH(val);
						//	console.log(fn);
						}	if(fn == 'progressbarI'){
							progressbarI(val);
						//	console.log(fn);
						}	if(fn == 'progressbarJ'){
							progressbarJ(val);
					//		console.log(fn);
						}	if(fn == 'progressbarK'){
							progressbarK(val);
						//	console.log(fn);
						}	if(fn == 'progressbarL'){
							progressbarL(val);
						//	console.log(fn);
						}	if(fn == 'progressbarM'){
							progressbarM(val);
						//	console.log(fn);
						}	if(fn == 'progressbarN'){
							progressbarN(val);
						//	console.log(fn);
						}if(fn == 'progressbarO'){
							progressbarO(val);
						//	console.log(fn);
						}if(fn == 'progressbarP'){
							progressbarP(val);
						//	console.log(fn);
						}if(fn == 'progressbarQ'){
							progressbarQ(val);
						//	console.log(fn);
						}if(fn == 'progressbarR'){
							progressbarR(val);
						//	console.log(fn);
						}if(fn == 'progressbarS'){
							progressbarS(val);
						//	console.log(fn);
						}if(fn == 'progressbarT'){
							progressbarT(val);
					//		console.log(fn);
						}if(fn == 'progressbarU'){
							progressbarU(val);
					//		console.log(fn);
						}if(fn == 'progressbarV'){
							progressbarV(val);
						//	console.log(fn);
						}if(fn == 'progressbarW'){
							progressbarW(val);
						//	console.log(fn);
						}if(fn == 'progressbarX'){
							progressbarX(val);
						//	console.log(fn);
						}if(fn == 'progressbarY'){
							progressbarY(val);
						//	console.log(fn);
						}if(fn == 'progressbarZ'){
							progressbarZ(val);
						//	console.log(fn);
						}

				});
			});

			$.each(alpha , function (index, value){
				$(".minus"+value).click(function () {

								var oldValue = document.getElementById('myRange'+value).value;
								if (oldValue > 0){
								var val = parseInt(oldValue) -1;
							} else {
								var val = parseInt(oldValue);
							}
							//	$('#theprogressbarA').attr('aria-valuenow', val).css('width', val+'%');
								var fn = 'progressbar'+value;
								$('#myRange'+value).val(val);
								$('#textvalue2'+value).text(val);
								if(fn == 'progressbarA'){
								progressbarA(val);
							}
							if(fn == 'progressbarB'){
								progressbarB(val);
								console.log(fn);
							}
							if(fn == 'progressbarC'){
								progressbarC(val);
								console.log(fn);
							}
							if(fn == 'progressbarD'){
								progressbarD(val);
								console.log(fn);
							}
							if(fn == 'progressbarE'){
								progressbarE(val);
								console.log(fn);
							}
							if(fn == 'progressbarF'){
								progressbarF(val);
								console.log(fn);
							}	if(fn == 'progressbarG'){
								progressbarG(val);
								console.log(fn);
							}	if(fn == 'progressbarH'){
								progressbarH(val);
								console.log(fn);
							}	if(fn == 'progressbarI'){
								progressbarI(val);
								console.log(fn);
							}	if(fn == 'progressbarJ'){
								progressbarJ(val);
								console.log(fn);
							}	if(fn == 'progressbarK'){
								progressbarK(val);
								console.log(fn);
							}	if(fn == 'progressbarL'){
								progressbarL(val);
								console.log(fn);
							}	if(fn == 'progressbarM'){
								progressbarM(val);
								console.log(fn);
							}	if(fn == 'progressbarN'){
								progressbarN(val);
								console.log(fn);
							}if(fn == 'progressbarO'){
								progressbarO(val);
								console.log(fn);
							}if(fn == 'progressbarP'){
								progressbarP(val);
								console.log(fn);
							}if(fn == 'progressbarQ'){
								progressbarQ(val);
								console.log(fn);
							}if(fn == 'progressbarR'){
								progressbarR(val);
								console.log(fn);
							}if(fn == 'progressbarS'){
								progressbarS(val);
								console.log(fn);
							}if(fn == 'progressbarT'){
								progressbarT(val);
								console.log(fn);
							}if(fn == 'progressbarU'){
								progressbarU(val);
								console.log(fn);
							}if(fn == 'progressbarV'){
								progressbarV(val);
								console.log(fn);
							}if(fn == 'progressbarW'){
								progressbarW(val);
								console.log(fn);
							}if(fn == 'progressbarX'){
								progressbarX(val);
								console.log(fn);
							}if(fn == 'progressbarY'){
								progressbarY(val);
								console.log(fn);
							}if(fn == 'progressbarZ'){
								progressbarZ(val);
								console.log(fn);
							}

					});
				});

			function progressbarA(val) {
				document.getElementById('textnameA').innerHTML = 'A-Aldehyde';

				document.getElementById('textvalueA').innerHTML = val;
				$('#theprogressbarA').attr('aria-valuenow', val).css('width', val*2+'%');

				updateValue();
				chartContent();
			}

			function progressbarB(val) {
				document.getElementById('textnameB').innerHTML = 'B-iceBerg';
					document.getElementById('textvalueB').innerHTML = val;
				$('#theprogressbarB').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}

			function progressbarC(val) {
				document.getElementById('textnameC').innerHTML = 'C-Citrus';
					document.getElementById('textvalueC').innerHTML = val;
				$('#theprogressbarC').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarD(val) {
				document.getElementById('textnameD').innerHTML = 'D-Dairy';
					document.getElementById('textvalueD').innerHTML = val;
				$('#theprogressbarD').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarE(val) {
				document.getElementById('textnameE').innerHTML = 'E-Edible';
					document.getElementById('textvalueE').innerHTML = val;
				$('#theprogressbarE').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarF(val) {
				document.getElementById('textnameF').innerHTML = 'F-Fruit';
					document.getElementById('textvalueF').innerHTML = val;
				$('#theprogressbarF').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarG(val) {
				document.getElementById('textnameG').innerHTML = 'G-Green';
				document.getElementById('textvalueG').innerHTML = val;
				$('#theprogressbarG').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarH(val) {
				document.getElementById('textnameH').innerHTML = 'H-Herb';
					document.getElementById('textvalueH').innerHTML = val;
				$('#theprogressbarH').attr('aria-valuenow', val).css('width', val*2+'%');

				updateValue();
				chartContent();
			}
			function progressbarI(val) {
				document.getElementById('textnameI').innerHTML = 'I-Iris';
					document.getElementById('textvalueI').innerHTML = val;
				$('#theprogressbarI').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}

			function progressbarJ(val) {
				document.getElementById('textnameJ').innerHTML = 'J-Jasmine';
					document.getElementById('textvalueJ').innerHTML = val;
				$('#theprogressbarJ').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarK(val) {
				document.getElementById('textnameK').innerHTML = 'K-Konifer';
						document.getElementById('textvalueK').innerHTML = val;
				$('#theprogressbarK').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarL(val) {
				document.getElementById('textnameL').innerHTML = 'L-Linalool';
					document.getElementById('textvalueL').innerHTML = val;
				$('#theprogressbarL').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarM(val) {
				document.getElementById('textnameM').innerHTML = 'M-Muguet';
					document.getElementById('textvalueM').innerHTML = val;
				$('#theprogressbarM').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarN(val) {
				document.getElementById('textnameN').innerHTML = 'N-Narcotic';
					document.getElementById('textvalueN').innerHTML = val;
				$('#theprogressbarN').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarO(val) {
				document.getElementById('textnameO').innerHTML = 'O-Orchid';
					document.getElementById('textvalueO').innerHTML = val;
				$('#theprogressbarO').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarP(val) {
				document.getElementById('textnameP').innerHTML = 'P-Phenol';
					document.getElementById('textvalueP').innerHTML = val;
				$('#theprogressbarP').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarQ(val) {
				document.getElementById('textnameQ').innerHTML = 'Q-Balsam';
					document.getElementById('textvalueQ').innerHTML = val;
				$('#theprogressbarQ').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarR(val) {
				document.getElementById('textnameR').innerHTML = 'R-Rose';
					document.getElementById('textvalueR').innerHTML = val;
				$('#theprogressbarR').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarS(val) {
				document.getElementById('textnameS').innerHTML = 'S-Spice';
					document.getElementById('textvalueS').innerHTML = val;
				$('#theprogressbarS').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarT(val) {
				document.getElementById('textnameT').innerHTML = 'T-Tar Smoke';
					document.getElementById('textvalueT').innerHTML = val;
				$('#theprogressbarT').attr('aria-valuenow', val).css('width', val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarU(val) {
				document.getElementById('textnameU').innerHTML = 'U-Animal';
					document.getElementById('textvalueU').innerHTML = val;
				$('#theprogressbarU').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarV(val) {
				document.getElementById('textnameV').innerHTML = 'V-Vanilla';
					document.getElementById('textvalueV').innerHTML = val;
				$('#theprogressbarV').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarW(val) {
				document.getElementById('textnameW').innerHTML = 'W-Wood';
					document.getElementById('textvalueW').innerHTML = val;
				$('#theprogressbarW').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarX(val) {
				document.getElementById('textnameX').innerHTML = 'X-Musk';
					document.getElementById('textvalueX').innerHTML = val;
				$('#theprogressbarX').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarY(val) {
				document.getElementById('textnameY').innerHTML = 'Y-Mossy';
					document.getElementById('textvalueY').innerHTML = val;
				$('#theprogressbarY').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();
			}
			function progressbarZ(val) {
				document.getElementById('textnameZ').innerHTML = 'Z-Zolvent';
					document.getElementById('textvalueZ').innerHTML = val;
				$('#theprogressbarZ').attr('aria-valuenow', val).css('width',  val*2+'%');
				updateValue();
				chartContent();

			}


				var data = [
					{
					data: value,
					labels: fullname,
					backgroundColor: color,
					borderColor: "#fff"
				}];


				var options = {
					tooltips: {
						enabled: true,
						callbacks: {
				 			 title: function(tooltipItems, data) {
				 				 return '';
				 			 },
				 			 label: function(tooltipItem, data) {
				 				 var datasetLabel = '';
				 				 var label = data.labels[tooltipItem.index];
				 				 return label;
				 				// return data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
				 			 }
				 		 },

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
										 animationSteps: 2000,
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
					plugins: {

						datalabels: {
							formatter: (value, ctx) => {

								var sum = 0;
								var dataArr = ctx.chart.data.datasets[0].data;
								var labell = ctx.chart.data.labels[ctx.dataIndex];
								var res = labell.split("-",1);

								dataArr.map(data => {
									sum += parseInt(data);

								});
								var percentage = (value*100 / sum).toFixed(0);
									return res+" "+percentage;


							},
							display: function(context) {
								var dis = context.dataset.data[context.dataIndex] >= 1;

								return dis;// or >= 1 or ...

							},
							color: '#00000f',
						}
					}

				};

				var ctx = document.getElementById("pie-chart").getContext('2d');
				var myChart = new Chart(ctx, {

					type: 'doughnut',
					data: {
						labels: fullname,
						datasets: data
					},

					options: options


				});


				function chartContent() {
				//	myChart.data.datasets[0].data.push = updateValue();


				myChart.data.datasets[0].data = updateValue();
				myChart.update();

				}
