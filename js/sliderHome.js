$(document).ready(function() {
    $('.slider').slick({
        arrows: true,
        dots: true,
        slidesToShow: 1,
        autoplay: true,
        speed: 1000,
        autoplaySpeed: 5000,
        responsive: [{
                breakpoint: 768,
                settings: {
                    arrows: false
                }
            },
            {
                breakpoint: 620,
                settings: {
                    arrows: false
                }
            },
            {
                breakpoint: 577,
                settings: {
                    arrows: false,
                    dots: true
                }
            }
        ]
    });
});