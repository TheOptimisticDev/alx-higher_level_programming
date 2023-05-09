// JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    $('DIV#hello').html(data.hello);
  });
});
