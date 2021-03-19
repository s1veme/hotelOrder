$('.review__btn').click(function() {
    $.post(
        '/api', // адрес обработчика
        $(".review-form").serialize(), // отправляемые данные  		
    );
});