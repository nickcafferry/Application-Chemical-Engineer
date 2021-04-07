// JavaScript Document

$(function(){

		//婊戣繃鍥炬爣鍚庯紝LOGO鎽嗗姩	
	$(".search_result li").mouseenter(function () {
		$(this).find(".logo").animate({
			'left': '35%'
		}, 500).animate({
			'left': '65%'
		}, 500);
	});


	$(".search_result li").mouseleave(function () {
		$(this).find(".logo").animate({
			'left': '50%'
		}, 1000);

	});
	$(".search_input").keyup(function (event) {
	    if (event.keyCode == 13) {
	        $("#form1").trigger("submit");
	    }
	});
	$(".search").keyup(function (event) {
	    if (event.keyCode == 13) {
	        $("#form1").trigger("submit");
	    }
	});

    //鐧惧害鎺ㄩ€�
	var bp = document.createElement('script');
	var curProtocol = window.location.protocol.split(':')[0];
	if (curProtocol === 'https') {
	    bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
	}
	else {
	    bp.src = 'http://push.zhanzhang.baidu.com/push.js';
	}
	var s = document.getElementsByTagName("script")[0];
	s.parentNode.insertBefore(bp, s);
})

function shw_prix(num){

	var a=document.getElementById("search_result");
	var price=a.getElementsByClassName("prix");
	var btn=a.getElementsByClassName("btn_box");
	/*alert(btn[0].style.width);*/		
	price[num].style.display="block";
	btn[num].style.display="none";
	
}

function shw_btn(num){
	var a=document.getElementById("search_result");
	var price=a.getElementsByClassName("prix");
	var btn=a.getElementsByClassName("btn_box");
	/*alert(btn[0].style.width);*/		
	price[num].style.display="none";
	btn[num].style.display="block";
	
}
