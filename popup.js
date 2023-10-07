/*
This is the popup.js file for the Google Chrome extension.
*/
document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('keydown', function(event) {
    if (event.altKey && event.key === 'n') {
      chrome.extension.getBackgroundPage().handle_key_binding(event);
    }
  });
});