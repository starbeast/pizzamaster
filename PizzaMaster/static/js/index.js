(function($) {
    $(document).ready(function() {
        var images = $('.cropped-image');
        var ind = 0;
        images.on('load', function() {
            ind++;
            var $this = $(this);
            console.log($this.css('height'), $this.css('width'));
            var offset = (140 - parseInt($this.css('width'))) / 2;
            $this.css('left', offset + 'px');
//                $this.off('load');
            if(ind == images.length) {
                $(".image-wrapper").colorbox({rel:'image-wrapper'
                    , opacity: 0.8
                    , fixed: true
                    , transition:"elastic"
                    , width: '60%'
                    , height: '60%'
                    , maxWidth: '80%'
                    , maxHeight: '80%'
                    , next: '<span class="arrow arrow-next"></span>'
                    , previous: '<span class="arrow arrow-previous"></span>'});
            }
        });
    });
})(jQuery);