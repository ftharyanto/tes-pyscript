document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.datepicker');
  options = {
    autoClose: true,
    format: 'dd-mm-yyyy'
  }
  M.Datepicker.init(elems, options);
});
