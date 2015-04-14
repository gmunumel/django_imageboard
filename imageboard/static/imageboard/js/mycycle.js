jQuery(function($){

    // Cycle plugin
    $('.slides').cycle({
      fx:     'none',
      speed:   800,
      timeout: 70
    }).cycle("pause");

    // Pause & play on hover
    $('.slideshow-block').hover(function(){
      $(this).find('.slides').addClass('active').cycle('resume');
      }, function(){
      $(this).find('.slides').removeClass('active').cycle('pause');
    });
});

