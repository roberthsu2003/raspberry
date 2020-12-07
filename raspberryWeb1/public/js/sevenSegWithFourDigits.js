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

//製作tab
$(function(){
    if(window.innerWidth > 991){
      $(".displayArea .tab").hide();
    }else{
       $(".tabcontent").hide().first().show();

    }
    $(window).resize(function(event){
        if(window.innerWidth > 991){
            $(".displayArea .tab").hide();
            $(".tabcontent").show();
            console.log("run");
        }else{
             $(".displayArea .tab").show();
             $(".tabcontent").hide().first().show();
        }
    });

    $('.tab').on("click",function(event){
        event.preventDefault();
        switch (event.target.textContent){
            case "攝氐":
                $(".tabcontent").hide().first().show();
                break;

            case "華氐":
                 $(".tabcontent").hide().eq(1).show();
                break;

           case "絕對溫度":
               console.log("kelvin");
               $(".tabcontent").hide().eq(2).show();
                break;

        }

    });
});

// Initialize Firebase
let database = firebase.database();


//firebase
$(document).ready(function(){
    //read firebase data of digit node
 database.ref("iot0624/temperature").on('value',function(snapshot){
       //console.log(snapshot.val())
        let cesValue = snapshot.val();
        let fahrenValue = cesValue * 1.8 + 32;
        let kelvinValue = cesValue + 273.15;
        $('#ces').text(cesValue.toFixed(2));
        $('#fahrenheit').text(fahrenValue.toFixed(2));
        $('#kelvin').text(kelvinValue.toFixed(2));

    });

});