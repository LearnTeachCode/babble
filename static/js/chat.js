window.onload = function() {
    var socket = new WebSocket("ws://localhost:8000/chatsock");
    var chatBox = document.getElementById("chatBox");
    var chatLog = document.getElementById("chatLog");
    var chatButton = document.getElementById("chatButton");

    chatButton.onclick = function() {
        socket.send(chatBox.value);
    };

    socket.onmessage = function(event) {
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(event.data));
        chatLog.appendChild(li);
    };
};
