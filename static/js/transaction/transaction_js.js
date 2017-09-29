/**
 * Created by shital on 9/29/17.
 */
$('body').on('change', '.item-list', function () {
    var item_list = $(this).val()
    $.ajax({
        type: 'GET',
        method: 'GET',
        url: '/items/' + + item_list  + '/get/unit_price' ,
        error: function () {
            console.log("error");
        },
        success: function (data) {
            // if (!$.trim(data)){
            //   topic.empty().append(new Option("Select Topic", " "))
            // }else{
            //   topic.empty().append(new Option("Select Topic", " "))
            //   for (var i = 0; i < data.length; i++) {
            //     var id = data[i].id;
            //     var title = data[i].name;
            //     topic.append(new Option(title, id));
            //   }
            // }
            // $('#overlay').hide();
           console.log(data);
        },
    });

});