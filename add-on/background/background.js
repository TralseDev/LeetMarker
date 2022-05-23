APP_NAME = "LeetMarker";


let port = browser.runtime.connectNative(`${APP_NAME}_native`);
console.log(`Conntected to native app`);

port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});


let portFromLeetMarker;

function connected(p) {
  portFromLeetMarker = p;
  portFromLeetMarker.postMessage("hi there content script!");
  portFromLeetMarker.onMessage.addListener(function (m) {
    sendMessage(m);
    portFromLeetMarker.postMessage("Sent! This: " + m.greeting);
  });
}

browser.runtime.onConnect.addListener(connected);


function u2b(str) {
  // utf8 to base64
  return window.btoa(unescape(encodeURIComponent(str)));
}

function b2u(str) {
  // base64 to utf8
  return decodeURIComponent(escape(window.atob(str)));
}

function sendMessage(message) {
  console.log(`Sending: ${message}`);
  //var sending = browser.runtime.sendNativeMessage(`${APP_NAME}_native`, message);
  //sending.then(onResponse, onError);
  try {
    port.postMessage(message);
  } catch (e) {
    console.log(`ERROR@${APP_NAME}: ${e}`);
  }
  console.log(`Sent!`);
}

function getSelectedText() {
  var text = "";
  if (typeof window.getSelection != "undefined") {
    text = window.getSelection().toString();
  } else if (typeof document.selection != "undefined" && document.selection.type == "Text") {
    text = document.selection.createRange().text;
  }
  return text;
}

function handle(selectedText = getSelectedText()) {
  var link = window.location.href;
  var headline = document.title;
  if (selectedText) {
    console.log(`Selected text: ${selectedText}`);
    console.log("Got selected text " + selectedText);
    try {
      navigator.clipboard.writeText(selectedText);
    } catch (e) {
      console.log(`ERROR@${APP_NAME}: Wasn't able to copy selected text to clipboard! -> ${e}`);
    }
    sendMessage(`${headline}|${selectedText}|${link}`);
  }
}

function ping() {
  sendMessage(`ping`);
}

function onResponse(response) {
  console.log("Received " + response);
}

function onError(error) {
  console.log(`Error@LeetMarker: ${error}`);
}

//document.addEventListener("mouseup", handle, false);

function onCreated() {
  if (browser.runtime.lastError) {
    console.log(`Error: ${browser.runtime.lastError}`);
  } else {
    console.log("Item created successfully");
  }
}

/*
Called when the item has been removed.
We'll just log success here.
*/
function onRemoved() {
  console.log("Item removed successfully");
}

/*
Called when there was an error.
We'll just log the error here.
*/
function onError(error) {
  console.log(`Error: ${error}`);
}

browser.menus.create({
  id: "log-selection",
  //type: "radio",
  title: "Save",
  contexts: ["selection"],
}, onCreated);

function updateCheckUncheck() {
  checkedState = !checkedState;
  if (checkedState) {
    browser.menus.update("check-uncheck", {
      title: browser.i18n.getMessage("menuItemUncheckMe"),
    });
  } else {
    browser.menus.update("check-uncheck", {
      title: browser.i18n.getMessage("menuItemCheckMe"),
    });
  }
}

browser.menus.onClicked.addListener((info, tab) => {
  switch (info.menuItemId) {
    case "log-selection":
      console.log(`Pressed, text: ${info.selectionText}`);
      handle(info.selectionText);
      break;
  }
});
handle();
console.log(`Loaded ${APP_NAME}`);