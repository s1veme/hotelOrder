$('.review__btn').click(function() {
    $.post(
        '/api/send-review',
        $(".review-form").serialize(),
    );
});


$('.button-request').click(function() {
    $.post(
        '/api/send-reservation',
        $(".reservation-form").serialize(),
    );
})