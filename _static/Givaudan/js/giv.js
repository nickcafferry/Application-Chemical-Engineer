// JavaScript Document


	$(function(){
/*	if(location.search.indexOf("?")==-1){
		location.href=location.search+"?a=1";
	}
		alert(location.search);*/
		
		
		w=$(window).width();
		h=parseInt(w*500/1440);

	$('#headerimg').css({'width':w+"px"});
	$('#headerimg').css({'height':h+"px"});	
	$('#giv_slide').css({'width':w+"px"});
	$('#giv_slide').css({'height':h+"px"});
	$('.inner_header').css({'height':"40%"});	
		
	$(".search_result li[class*='reco']").mouseenter(		
	function(){
		$(this).find('.btn_box').css({'display':'block'});
		$(this).find('.prix').css({'display':'none'});
	});	
		
	$(".search_result li[class*='reco']").mouseleave(		
	function(){
		$(this).find('.prix').css({'display':'block'});
		$(this).find('.btn_box').css({'display':'none'});
	});			

	//婊氬姩鏉℃帶鍒�
	$('.prod_link').jScrollPane(
			{
		hijackInternalLinks: true
			}
	);
		
		
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
