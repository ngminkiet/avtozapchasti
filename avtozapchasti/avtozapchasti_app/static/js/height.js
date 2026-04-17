let bodyHeight = $(document).height() - $('footer').height();

//Если высота экрана сходится с высотой документа
if($(window).height() == $(document).height()) {
    $('main').css('height', bodyHeight + 'px');
}