/**
 * Created by shital on 9/29/17.
 */
var item_price = 0;

$(document).ready(function () {
    var item_list = $(".item-list").val();
    // alert(item_list);
    if (item_list) {
        $.ajax({
            type: 'GET',
            method: 'GET',
            url: '/items/' + item_list + '/get/unit_price',
            error: function () {
                console.log("error");
            },
            success: function (data) {
                item_price = data;
                if (item_quantity.length != 0) {
                    var total = item_price * item_quantity;
                    $('.total-cost').val(total);
                    // console.log('Total: ' + total)
                }
            },
        });
    }
});

(function ($) {
    $.fn.filter_select = function () {
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
    }
})(jQuery);

$('body').on('change', '.item-list', function () {
    var item_list = $(this).val();
    var item_quantity = $('.item-quantity').val();
    if (item_list) {
        $.ajax({
            type: 'GET',
            method: 'GET',
            url: '/items/' + item_list + '/get/unit_price',
            error: function () {
                console.log("error");
            },
            success: function (data) {
                item_price = data;
                if (item_quantity.length != 0) {
                    var total = item_price * item_quantity;
                    $('.total-cost').val(total);
                }
            },
        });
    }else {
        item_price = 1;
    }
});

$('body').on('input', '.item-quantity', function () {
    var item_quantity = $('.item-quantity').val();
    if ($('.item-list option:selected').text().length != 0) {
        var total = item_price * item_quantity;
        $('.total-cost').val(total);
    }
});

$('body').on('change', '#filter', function () {
    $(document).filter_select();
});

$(document).ready(function () {
    if (window.location.href.indexOf("&start_date") > -1) {
        $("select option").each(function () {
            if ($(this).text() == 'Date')
                $(this).attr("selected", "selected");
        });
    } else if (window.location.href.indexOf("&item_name") > -1) {
        $("select option").each(function () {
            if ($(this).text() == 'Item Name')
                $(this).attr("selected", "selected");
        });
    }
    $(document).filter_select();
    $('.datepicker').nepaliDatePicker();

    $('.created-date').each(function () {
        $(this).text(AD2BS($(this).text()));
    });
});


