function addToCartAjax(id) {
    $.ajax({
        url: "/check_product_exist/",
        type: "POST",
        dataType: "JSON",
        data: {
            "product_id": id,
            // "instance": instance,
            // "storeId": storeId,
            // "_token": "wy4c136LVo5KnpK03FKr1pSZZddhehoiewKdJV7s"
        },
        async: false,
        success: function (response) {
            if(response["valid"]) {
                let isExist = false;
                alertJs('success', "Add product to cart successfully");
                let count_cart = parseInt(localStorage.getItem('count_cart')) + 1;
                localStorage.setItem('count_cart', count_cart.toString());
                $('.sc-cart').html(count_cart);
                // add object to localStorage
                var list_cart = JSON.parse(localStorage.getItem('list_cart'));
                // let instance = JSON.parse(response["new_comment"]);
                // let fields = instance[0]["fields"];
                for (let i = 0; i< list_cart.length ; i++ )
                    if (list_cart[i].id === id){
                        isExist = true;
                        list_cart[i].qty += 1;
                    }
                if (!isExist){
                    list_cart.push({"id": id, "qty": 1});
                }
                localStorage.setItem('list_cart', JSON.stringify(list_cart));
            }
        },

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