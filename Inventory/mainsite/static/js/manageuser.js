$(document).ready(function(){
    var entryend = document.getElementById('termnentry');
    $('table tbody > tr').slice(0,10).show();
    //search function
     $("#searchInp").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#userTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
})

function changeTermEntry(this_){
    $('table tbody tr').hide();
    const trs = document.getElementById('userTable').rows;
    document.getElementById('termnentry').innerText=this_.value;
    document.getElementById('termnentry').value=this_.value;
    $('table tbody > tr').slice(0,parseInt(this_.value)).show();
    return;
}
function reverse_cols(){
$("table td").each(function() {
  $(this).parent().prepend(this);
});
}