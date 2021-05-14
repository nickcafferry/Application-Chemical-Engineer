function percentage(num, per)
{
	return (num/100)*per;
}

function max(input) {
	if (toString.call(input) !== "[object Array]")
	return false;
	return Math.max.apply(null, input);
}
function indexOfMax(arr) {
	if (arr.length === 0) {
		return -1;
	}

	var max = arr[0];
	var maxIndex = 0;

	for (var i = 1; i < arr.length; i++) {
		if (arr[i] > max) {
			maxIndex = i;
			max = arr[i];
		}
	}

	return maxIndex;
}
function sum(input){

	if (toString.call(input) !== "[object Array]")
	return false;

	var total =  0;
	for(var i=0;i<input.length;i++)
	{
		if(isNaN(input[i])){
			continue;
		}
		total += Number(input[i]);
	}
	return total;
}
function roundToTwo(num) {
	return +(Math.round(num + "e+1")  + "e-1");
}

function clickBack() {
var txt;
var r = confirm("Go Back to start a new formula?\nCancel to save this formula first.");
if (r == true) {
	window.location.href = "index.php";
} else {
  txt = "You pressed Cancel!";
}

}
