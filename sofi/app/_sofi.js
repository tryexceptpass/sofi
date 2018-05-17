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
        console.log(command)

        if (command.name == "init") {
            if (command.html)
                d3.select("html").html(command.html)

            load()
        }
        else if (command.name == "append") {
            $(command.selector).append(command.html)
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
            if (command.text == null) {
                var resp = {'event': 'response', 'request_id': command.request_id, 'text': d3.select(command.selector).text()}
                console.log(resp)
                socket.send(JSON.stringify(resp))
            }
            else {
                d3.selectAll(command.selector).text(command.text)
            }
        }
        else if (command.name == "attr") {
            if (command.text == null) {
                var resp = {'event': 'response', 'request_id': command.request_id, 'attr': d3.select(command.selector).attr(command.attr)}
                console.log(resp)
                socket.send(JSON.stringify(resp))
            }
            else {
                d3.selectAll(command.selector).attr(command.attr, command.value)
            }
        }
        else if (command.name == "style") {
            if (command.priority) {
                d3.selectAll(command.selector).style(command.style, command.value, command.priority)
            }
            else {
                d3.selectAll(command.selector).style(command.style, command.value)
            }
        }
        else if (command.name == "property") {
            if (command.text == null) {
                var resp = {'event': 'response', 'request_id': command.request_id, 'prop': d3.select(command.selector).property(command.property)}
                console.log(resp)
                socket.send(JSON.stringify(resp))
            }
            else {
                d3.selectAll(command.selector).property(command.property, command.value)
            }
        }
        else if (command.name == "subscribe") {
            var key = command.key
            d3.selectAll(command.selector).on(command.event + "." + key, function(d,i) {
                var eventTarget = d3.event.target || d3.event.srcElement;
                socket.send(JSON.stringify({ "event": d3.event.type,
                                             "element": eventTarget.id,
                                             "event_object": getProperties(d3.event),
                                             "d": d,
                                             "i": i,
                                             "key": key
                                           }))
            }, command.capture)
        }
        else if (command.name == "unsubscribe") {
            d3.selectAll(command.selector).on(command.event + "." + command.key, null)
        }
    }
}


function getAllPropertyNames(obj) {
    var props = [];

    do {
        props = props.concat(Object.getOwnPropertyNames(obj))
    } while (obj = Object.getPrototypeOf(obj))

    return props
}

function getProperties(obj) {
    newObj = {}
    props = getAllPropertyNames(obj)
    console.log(obj)
    props.forEach(function(p) {
        propType = typeof obj[p]
        if (propType == "object") {
            if (obj[p] instanceof HTMLElement) {
                newObj[p] = { }
                newObj[p]['innerText'] = obj[p].innerText
                newObj[p]['outterText'] = obj[p].outterText
                newObj[p]['innerHTML'] = obj[p].innerHTML
                newObj[p]['outterHTML'] = obj[p].outterHTML
                newObj[p]['textContent'] = obj[p].textContent
                newObj[p]['value'] = obj[p].value

                for (var i = 0; i < obj[p].attributes.length; i++) {
                    newObj[p][obj[p].attributes[i].name] = obj[p].attributes[i].value
                }
            }
        }
        else if (propType != "function") {
            if (obj[p] != null)
                newObj[p] = obj[p].toString()
            else {
                newObj[p] = null
            }
        }
    })

    return newObj
}

function load() {
    socket.send(JSON.stringify({ "event": "load" }))
}

window.onload = function(event) {
    init()
}
