//menu
$(function () {
    $.ajax({
        dataType: "json",
        url: "menu.json",
        success: function(data){
            var menuHtml = "";
            jQuery.each(data,function(key,value){
                menuHtml += "<li><a href=\""+ value + "\">" + key + "</a></li>\n";
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

//firebase
$(function () {
   var firebaseConfig = {
    apiKey: "AIzaSyCBa3cc1A9mlWzDnG_0e9ltIcZhOWiA-tk",
    authDomain: "arduinofirebase-6d104.firebaseapp.com",
    databaseURL: "https://arduinofirebase-6d104.firebaseio.com",
    projectId: "arduinofirebase-6d104",
    storageBucket: "arduinofirebase-6d104.appspot.com",
    messagingSenderId: "775007261514",
    appId: "1:775007261514:web:1d7170ca43c85472"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
});