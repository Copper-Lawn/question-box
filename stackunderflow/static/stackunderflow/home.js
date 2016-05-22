$(function () {
    var elem = $('#userGroup'),
        elemTop = elem.offset().top;
    $(window).scroll(function () {
        elem.toggleClass('fixed', $(window).scrollTop() > elemTop);
    }).scroll();
});
