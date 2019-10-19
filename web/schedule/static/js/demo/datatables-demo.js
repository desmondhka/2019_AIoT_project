// Call the dataTables jQuery plugin
function getDataOfDay(date) {
  location.href = "/schedule/"+date;
}

$(document).ready(function() {
  $('#dataTable').DataTable( {
    "paging": false,
  });
  $( "#datepicker" ).datepicker( {
  	dateFormat: "yy-mm-dd",
  	maxDate: new Date( 2019, 8, 29, 8, 15 ),
  	minDate: new Date( 2019, 2, 22, 8, 15 ),
  });
});
