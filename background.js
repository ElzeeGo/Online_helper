/*
This is the background.js file for the Google Chrome extension.
*/
function handle_key_binding(event) {
  if (event.name === 'n' && event.altKey) {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'activate_chat_gpt' });
    });
  }
}
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === 'get_active_element') {
    chrome.tabs.executeScript(
      { code: 'document.activeElement.tagName' },
      function (result) {
        sendResponse(result[0]);
      }
    );
    return true;
  }
});
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === 'generate_prompt') {
    var prompt = 'User: ' + message.activeElement + '\nAI: ';
    sendResponse(prompt);
  }
});