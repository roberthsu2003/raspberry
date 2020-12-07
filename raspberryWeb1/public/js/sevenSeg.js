//menu
$(function () {
    $.ajax({
        dataType: "json",
        url: "../menu.json",
        success: function(data){
            var menuHtml = "";
            jQuery.each(data,function(key,value){
                menuHtml += "<li><a href=\"/"+ value + "\">" + key + "</a></li>\n";
            });

            $("nav ul").append(menuHtml);
        }
    });


});

//sign in
$(function(){
    let $alertMessage = $(".alertMessage");
    $alertMessage.hide();
    $('.signIn').on('click',function(event){
         $alertMessage.slideDown(400);
        event.preventDefault();
        $('.cancel').on("click",function(event){
            $alertMessage.slideUp(400);
        })
    });

});

//menu
$(function(){
    var menuState = false;
    $("#menu").on("click touchstart",function(event){
        menuState = !menuState;
        let smallWindow = $(window).width() <= 767;
        if (menuState && smallWindow) {
            console.log("menu open");
            $(this).attr("src","images/close.png");
            $("nav>ul").css("display","block");
        }else{
            console.log("menu close");
            $(this).attr("src","images/menu.png");
            $("nav>ul").css("display","none");
        }
        event.preventDefault();
    });
    $(window).resize(function(event){
        //console.log(window.innerWidth)
        if(window.innerWidth > 767){
            $("nav>ul").show();
        }
    });
});

// Initialize Firebase
let database = firebase.database();


//firebase
$(document).ready(function(){
    //read firebase data of digit node
    let iot0624Ref = database.ref('iot0624');
    iot0624Ref.child("digit").on('value',function(snapshot){
        let selectedValue = snapshot.val();
        $(".digits button").removeClass("selected").each(function(index,element){
            if(index == selectedValue){
               $(element).addClass("selected");
            }
        });
    });

    $(".digits").on("click",function (event) {
        let contentText = event.target.innerText;
        iot0624Ref.update({'digit':parseInt(contentText)});

    });
});