// JavaScript Document

$(function () {


    $('div[class*=btn]').mouseenter(function () {
        $(this).animate({ 'width': '35px' }, 500)
        var txt = $(this).text();

        if (txt == "详") {
            $(this).text("详情");
        }
        if (txt == "样")
        { $(this).text("样品"); }

        if (txt == "买")
        { $(this).text("购买"); }

        if (txt == "询")
        { $(this).text("询价"); }
    })

    $('div[class*=btn]').mouseleave(function () {
        $(this).animate({ 'width': '20px' }, 500)

        var txt = $(this).text();

        if (txt == "详情") {
            $(this).text("详");
        }
        if (txt == "样品")
        { $(this).text("样"); }

        if (txt == "购买")
        { $(this).text("买"); }

        if (txt == "询价")
        { $(this).text("询"); }
    })
    $('.searchstr').keydown(function () { if (event.keyCode == "13") $("#form1").trigger("submit"); })

    //百度推送
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
function checkbox(fields,dd) {
    var oi = $("#"+dd).is(":checked");
    if (oi)
        $("#key2").val(fields);
    else
        $("#key2").val('');
    $("#form1").trigger("submit");
}
