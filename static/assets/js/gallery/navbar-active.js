$(document).ready(function () {
    $('.navbar-nav li a').click(function(event) {

//        alert("Your book is overdue.");
//        console.log("sdfsdf");
        var href = $(this).attr('href');
        alert(href);

        $(this).addClass('active');
        //remove all pre-existing active classes
        $('.active').removeClass('active');


        var href2 = "portfolio:index2";

        event.preventDefault();
        $('#content').load(href2);
    });
});
