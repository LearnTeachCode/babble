var root = document.body;

var chat = {};

// chat component View-Model
chat.vm = {
    init: function() {
        chat.vm.logMessage = function(message) {
            if (message) {
                chat.vm.log.push(message);
            }
        }
        chat.vm.add = function() {
            if (chat.vm.message()) {
                chat.chatLog.push(chat.vm.message());
                chat.vm.message = null;
            }
        }
    },
    log: new Array,
    message: m.prop("")
}

chat.view = function () {
    return m("div", [
        m("ul", [
            chat.vm.log.map(function(val, index) {
                return m("li", val);
            })
        ]),
        m("input", { message: chat.vm.message() }),
        m("button", { onClick: chat.vm.add } , "Send")
    ]);
};

chat.controller = function() {
    chat.vm.init();
};

var component = {
    view: chat.view,
    controller: chat.controller
}

m.mount(root, component);