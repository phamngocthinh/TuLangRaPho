// // var count_cart = 0;
// var count_cart = parseInt(localStorage.getItem('count_cart'));
//                 localStorage.setItem('count_cart', count_cart.toString());
//                 $('.sc-cart').html(count_cart);
// // sessionStorage.setItem('cart', count_cart.toString());
// if (localStorage.getItem("count_cart") == null) {
//     localStorage.setItem('count_cart', '0');
//
// }
// else{
//     count_cart = parseInt(localStorage.getItem('count_cart')) + 1;
//     console.log(count_cart);
//     $('.sc-cart').html(count_cart);
// }
// // function myFunction(){
// //    console.log("THinhhhhhhhhhhhh");
// // }

function addToCartAjax(id) {
    // alert("document ready occurred!");
    $.ajax({
        url: "/post_friend/",
        type: "POST",
        dataType: "JSON",
        data: {
            "product_id": id,
            // "instance": instance,
            // "storeId": storeId,
            // "_token": "wy4c136LVo5KnpK03FKr1pSZZddhehoiewKdJV7s"
        },
        async: false,
        success: function (data) {
            if (data.is_taken) {
                // setTimeout(function () {
                //     if (data.instance == 'default') {
                //         $('.sc-cart').html(data.count_cart);
                //     } else {
                //         $('.sc-' + data.instance).html(data.count_cart);
                //     }
                // }, 1000);
                alertJs('success', "Add product to cart successfully");
                // alertJs('success', "aa");
                // var count_cart = 10;
                var count_cart = parseInt(localStorage.getItem('count_cart')) + 1;
                localStorage.setItem('count_cart', count_cart.toString());
                $('.sc-cart').html(count_cart);
                // alertJs('success', data.msg);
                // add object to localStorage

            } else {
                if (data.redirect) {
                    window.location.replace(data.redirect);
                    return;
                }
                alertJs('error', data.msg);
            }

        }
    });
}

function alertJs(type = 'error', msg = '') {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
    });
    Toast.fire({
        type: type,
        title: msg
    })
}

function alertMsg(type = 'error', msg = '', note = '') {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: true,
    });
    swalWithBootstrapButtons.fire(
        msg,
        note,
        type
    )
}

function formatNumber(num) {
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
}

$('#shipping').change(function () {
    $('#total').html(formatNumber(parseInt(0) + parseInt($('#shipping').val())));
});

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = '//connect.facebook.net/vi_VN/sdk.js#xfbml=1&version=v2.8&appId=934208239994473';
    fjs.parentNode.insertBefore(js, fjs);
}
(document, 'script', 'facebook-jssdk'))