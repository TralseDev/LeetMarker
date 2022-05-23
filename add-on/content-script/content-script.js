APP_NAME = "LeetMarker";


let myPort = browser.runtime.connect({name:"port-from-leetmarker"});

myPort.onMessage.addListener(function(m) {
  console.log("In content script, received message from background script: ");
  console.log(m.greeting);
});


function sendMessage(message) {
    myPort.postMessage(message);
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

function handle() {
    var link = window.location.href;
    var selectedText = getSelectedText()
    var headline = document.title;
    if (selectedText) {
        console.log(`Selected text: ${selectedText}`);
        console.log("Got selected text " + selectedText);
        try {
            navigator.clipboard.writeText(selectedText);
        } catch (e) {
            console.log(`ERROR@${APP_NAME}: Wasn't able to copy selected text to clipboard! -> ${e}`);
        }
        sendMessage(`${headline}-|||-${selectedText}-|||-${link}`);
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

document.addEventListener("mouseup", handle, false);

console.log(`Loaded ${APP_NAME}`);
