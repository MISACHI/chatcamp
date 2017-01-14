jQuery(document).ready(function(){
		$("#user-data").popover();
		$("#pwd-data").popover();
		$(".auto_animate").fadeIn(1000);

		$(".nav-tabs a:first").tab("show");

		var window_width = $(window).width();

		if (window_width <= 1500) {

			 $("#padding-top").addClass("padding-top-10");
			 $("#bottom-footer").removeClass("bottom-footer");
			 $("#copy-right").removeClass("col-md-7");
			 $("#copy-right").addClass("row");
			 /*$("#copy-right").addClass("col-xs-offset-3");*/
			 $("#footer-link").removeClass("col-md-5");
			 $("#footer-link").addClass("col-xs-12");
			 $("#address").removeClass("col-md-5");
			 /*$("#address").addClass("col-xs-offset-3");*/
			 $("#footer-link").addClass("row");
			 $("#footer-link").addClass("padding-top-10");
			 $("#footer-link").removeClass("footer-nav");
			 $("#footer-link").toggleClass("footer-nav-inline","footer-nav-inline2");
			 $("#push").addClass("col-sm-pull-4");
			 $("#pull").addClass("col-sm-push-4");
			 $("#push").addClass("col-sm-offset-4");
			 $("#pull").addClass("col-sm-offset-4");
			 $(".footer-center").addClass("text-center");
			 $(".push").addClass("text-center");
			 $(".row-margin-bottom").append("<hr>");
			 $(".row-margin-bottom").addClass("col-xs-offset-1");
			 $(".box").css("width","100px");
			 $("#spin").css("margin-bottom","10px");
			 $("#remove-align-right").removeClass("text-right");
			 $("#remove-align-right").addClass("text-center");
			 $("#align-center").addClass("text-center");
			 $("#remove-panel-fixed").removeClass("panel-fixed");

		}

});