// JavaScript Document

$(function () {


    $('div[class*=btn]').mouseenter(function () {
        $(this).animate({ 'width': '35px' }, 500)
        var txt = $(this).text();

        if (txt == "璇�") {
            $(this).text("璇︽儏");
        }
        if (txt == "鏍�")
        { $(this).text("鏍峰搧"); }

        if (txt == "涔�")
        { $(this).text("璐拱"); }

        if (txt == "璇�")
        { $(this).text("璇环"); }
    })

    $('div[class*=btn]').mouseleave(function () {
        $(this).animate({ 'width': '20px' }, 500)

        var txt = $(this).text();

        if (txt == "璇︽儏") {
            $(this).text("璇�");
        }
        if (txt == "鏍峰搧")
        { $(this).text("鏍�"); }

        if (txt == "璐拱")
        { $(this).text("涔�"); }

        if (txt == "璇环")
        { $(this).text("璇�"); }
    })
    $('.searchstr').keydown(function () { if (event.keyCode == "13") $("#form1").trigger("submit"); })

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
function checkbox(fields,dd) {
    var oi = $("#"+dd).is(":checked");
    if (oi)
        $("#key2").val(fields);
    else
        $("#key2").val('');
    $("#form1").trigger("submit");
}