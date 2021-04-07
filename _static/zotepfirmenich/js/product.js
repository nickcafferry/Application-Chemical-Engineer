// JavaScript Document
// JavaScript Document
$(function () {
	//璁剧疆鎶ご鍥鹃珮瀹�
	var w = document.documentElement.clientWidth;
	var h = parseInt(w / 2.88) + "px";
	headerimg.style.height = h;


	//婊戣繃浜у搧鍚庯紝LOGO涓婁笅鎽嗗姩	
	$(".brief0").mouseenter(function () {
		$(this).find(".logo").animate({
			'top': '150px'
		}, 1000);
	});


	$(".brief0").mouseleave(function () {
		$(this).find(".logo").animate({
			'top': '30px'
		}, 1000);

	});

	
	//婊戣繃浜у搧鍚庯紝LOGO涓婁笅鎽嗗姩	
	$(".download td").mouseenter(function () {
		$(this).find(".btn_dl").animate({
			'margin-left':(-40-20)+'px'
		}, 500).animate({
			'margin-left':(-40+20)+'px'
		},500);
	});


	$(".download td").mouseleave(function () {
		$(this).find(".btn_dl").animate({
			'margin-left': '-40px'
		}, 1000);

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
