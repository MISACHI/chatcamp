$(document).ready(function () {
    $("#notifications").popover();
    var window_width = $(window).width();
    if (window_width <= 1543) {
        $('#navbar-container .navbar-right').removeClass('col-sm-4');
        $('#navbar-container .navbar-right').addClass('col-sm-8');
    }
    if (window_width <= 882){
        $('#navbar-container .navbar-right').removeClass('col-sm-8');
        $('#navbar-container .navbar-right').addClass('col-sm-11');
	}
});