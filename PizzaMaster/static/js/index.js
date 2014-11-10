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
                $(".image-wrapper").colorbox({rel:'image-wrapper', transition:"fade"});
            }
        });
    });
})(jQuery);