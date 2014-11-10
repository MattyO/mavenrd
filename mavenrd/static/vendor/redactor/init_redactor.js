//$.ajaxSetup({
//    beforeSend: function(xhr, settings) {
//        console.log("setting up stuff");
//        //console.log(document.cookie);
//        xhr.setRequestHeader("X-CSRFToken", "test");
//    }
//});

$(document).ready(function(){
    $('.redactor').redactor({ 
        autoresize: false, 
        imageUpload: '/upload', 
        fileUpload: '/upload'

    });

});
