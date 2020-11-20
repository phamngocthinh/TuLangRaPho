function addToCartAjax(id, instance = null, storeId = null) {
    $.ajax({
        url: "https://demo.s-cart.org/add_to_cart_ajax",
        type: "POST",
        dataType: "JSON",
        data: {
            "id": id,
            "instance": instance,
            "storeId": storeId,
            "_token": "wy4c136LVo5KnpK03FKr1pSZZddhehoiewKdJV7s"
        },
        async: false,
        success: function (data) {
            // console.log(data);
            error = parseInt(data.error);
            if (error == 0) {
                setTimeout(function () {
                    if (data.instance == 'default') {
                        $('.sc-cart').html(data.count_cart);
                    } else {
                        $('.sc-' + data.instance).html(data.count_cart);
                    }
                }, 1000);
                alertJs('success', data.msg);
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