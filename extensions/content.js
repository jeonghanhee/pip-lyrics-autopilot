// content.js
var target_video = null;
var org_content;

function sendLyrics() {
    if (!enabled) return;

    const caption_element = document.getElementById("ytp-caption-window-container");
    if (caption_element != undefined && caption_element != null) {
        const msg = caption_element.textContent;

        if (msg != org_content) {
            org_content = msg;
            chrome.runtime.sendMessage({
                type: "SEND_MESSAGE_ONLY_LYRICS",
                content: msg
            })
        }
    }
}

// Event listener for entering/exiting PiP
document.addEventListener('enterpictureinpicture', () => {
    enabled = true;
    chrome.runtime.sendMessage({
        type: "CONNECT"
    })
    setInterval(() => sendLyrics(), 100);
});

document.addEventListener('leavepictureinpicture', () => {
    enabled = false;
});