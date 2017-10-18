/**
 * Created by shital on 10/18/17.
 */
$('body').on('change','.cash-paid',function () {
   var data = $(this).val();
   alert(data);
   // location.href = {% url 'transaction_cash_paid' pk=data%} ;
});
