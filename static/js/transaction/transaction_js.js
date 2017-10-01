/**
 * Created by shital on 9/29/17.
 */
var item_price = 0;

$('body').on('change', '.item-list', function () {
    var item_list = $(this).val();
    var item_quantity = $('.item-quantity').val();
    $.ajax({
        type: 'GET',
        method: 'GET',
        url: '/items/' + item_list + '/get/unit_price',
        error: function () {
            console.log("error");
        },
        success: function (data) {
            item_price = data;
            // console.log('price: ' + data);
            // console.log("Length: " + item_quantity.toString().length);
            if (item_quantity.toString().length != 0) {
                var total = item_price * item_quantity;
                $('.total-cost').val(total);
                // console.log('Total: ' + total)
            }
        },
    });
});

$('body').on('input', '.item-quantity', function () {
    var item_quantity = $('.item-quantity').val();
    if ($('.item-list option:selected').text().length != 0) {
        var total = item_price * item_quantity;
        $('.total-cost').val(total);
    }
});

$('body').on('change', '#filter', function () {
    if ($('#filter option:selected').text() == 'Date') {
        $('.item-name-content').addClass('hide');
        $('.date-content').removeClass('hide');
    } else if ($('#filter option:selected').text() == 'Item Name') {
        $('.item-name-content').removeClass('hide');
        $('.date-content').addClass('hide');
    } else {
        $('.item-name-content').addClass('hide');
        $('.date-content').addClass('hide');
    }
});
