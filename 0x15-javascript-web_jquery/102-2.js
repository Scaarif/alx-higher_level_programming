// fetches and prints how to say “Hello” depending on the language.

const $ = window.$;

$(document).ready(function () {
  // Attach an event handler for Enter keypress
  $('INPUT#language_code').keypress(function (eventObj) {
    if (eventObj.which === 13) {
      // Enter key-code pressed; get language code
      const langCode = $(this).val(); // get input value
      const translator = 'https://hellosalut.stefanbohacek.dev/';
      // Get the translation and display
      $.get(translator + '?lang=' + langCode, function (responseBody) {
        $('DIV#hello').text(`${responseBody.hello}`);
      });
    }
  });

  // Also trigger on clicking translate button
  $('INPUT#btn_translate').on('click', () => {
    $('INPUT#language_code').keypress();
  });
});
