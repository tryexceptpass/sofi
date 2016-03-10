
var SOCKET_URL = "ws://127.0.0.1:9000"
var socket

function init() {
    socket = new WebSocket(SOCKET_URL)

    socket.onopen = function(event) {
        console.log("Connected to websocket server at " + SOCKET_URL)
        socket.send(JSON.stringify({ "event": "init" }))
    }

    socket.onmessage = function(event) {
        console.log("Received: " + event.data)

        command = JSON.parse(event.data)

        if (command.name == "init") {
            if (command.html)
                d3.select("html").html(command.html)

            load()
        }
        else if (command.name == "append") {
            d3.selectAll(command.selector).append(command.html)
        }
        else if (command.name == "remove") {
            d3.selectAll(command.selector).remove()
        }
        else if (command.name == "replace") {
            d3.selectAll(command.selector).html(command.html)
        }
        else if (command.name == "addclass") {
            d3.selectAll(command.selector).classed(command.cl, true)
        }
        else if (command.name == "removeclass") {
            d3.selectAll(command.selector).classed(command.cl, false)
        }
        else if (command.name == "text") {
            d3.selectAll(command.selector).text(command.text)
        }
        else if (command.name == "attr") {
            d3.selectAll(command.selector).attr(command.attr, command.value)
        }
        else if (command.name == "style") {
            d3.selectAll(command.selector).style(command.style, command.value, command.priority)
        }
        else if (command.name == "property") {
            d3.selectAll(command.selector).property(command.property, command.value)
        }
    }
}

function load() {
    socket.send(JSON.stringify({ "event": "load" }))
}

window.onload = function(event) {
    init()
}