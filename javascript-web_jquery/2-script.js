const $ = window.$;

$('DIV#red_header').click(function (e) {
  $(e.target).css('color', 'red');
});
