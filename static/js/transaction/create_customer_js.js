/**
 * Created by shital on 10/13/17.
 */

$('body').on('click', '#create-customer', function () {
    var customer_form = $("#customer-form");
    var customer_list = $("#customer-list");
    customer_form.removeClass("hide");
    customer_list.removeClass("show");
    customer_list.addClass("hide");
    $(".customer-list").val("1");
});

$('body').on('click', '#cancle-customer', function () {
    var customer_form = $("#customer-form");
    var customer_list = $("#customer-list");
    customer_form.addClass("hide");
    customer_form.removeClass("show");
    customer_list.removeClass("hide");
    customer_list.addClass("show");
    $(".customer-list").val("");
});

