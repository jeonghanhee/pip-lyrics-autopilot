//background.js
var connected = false;
var port = null;
var enabled = false;

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    switch (request.type) {
        case "SEND_MESSAGE_ONLY_LYRICS":
            port.postMessage(request.content);
            break;
        case "SEND_VIDEO_DATA":
            console.log(request._frameInfo);
            break;
        case "CONNECT":
            if (connected) return;

            port = chrome.runtime.connectNative('com.my_company.my_application');
            connected = true;
            port.onDisconnect.addListener(function() {
                connected = false;
            });
            break;
    }
});