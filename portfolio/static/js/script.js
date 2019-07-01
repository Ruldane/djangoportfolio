$(function(){

    $(".navbar a, footer a").on("click", function(event){

        event.preventDefault();
        var hash = this.hash;

        $('body,html').animate({scrollTop: $(hash).offset().top} , 900 , function(){window.location.hash = hash;})

    });

  $(window).resize(function() {
	$('h1, h2, h3, h4 p').css('z-index', 'auto'); //auto reflow
  });


})