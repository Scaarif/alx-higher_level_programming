// fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

const $ = window.$;

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (responseData, textStatus) {
    $('DIV#hello').text(`${responseData.hello}`);
  });
});
