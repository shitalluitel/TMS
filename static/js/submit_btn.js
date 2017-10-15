/**
 * Created by shital on 10/15/17.
 */
$('form').submit(function() {
  $(this).find("button[type='submit']").prop('disabled',true);
});
