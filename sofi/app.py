import asyncio
import os

import json
import webbrowser

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol

class Sofi(object):
    def __init__(self):
        self.processor = SofiEventProcessor()
        self.server = SofiEventServer(processor=self.processor)

    def start(self):
        ### Start the application

        self.server.start()

    def register(self, event, callback, selector=None):
        ### Register event callback

        self.processor.register(event, callback, selector)

class SofiEventProcessor(object):
    """Event handler providing hooks for callback functions"""

    handlers = { 'init': { '_': [] },
                 'load': { '_': [] },
                 'close': { '_': [] },
                 'click': { '_': [] },
                 'mousedown': { '_': [] },
                 'mouseup': { '_': [] },
                 'keydown': { '_': [] },
                 'keyup': { '_': [] },
                 'keypress': { '_': [] }
               }

    def register(self, event, callback, selector=None):
        if event not in self.handlers:
            self.handlers[event] = { '_': [] }

        if selector:
            key = str(id(callback))
        else:
            key = '_'

        if key not in self.handlers[event]:
            self.handlers[event][key] = list()

        self.handlers[event][key].append(callback)

        if event not in ('init', 'load', 'close') and len(self.handlers[event].keys()) > 1:
            capture = False
            if selector is None:
                selector = 'html'
                capture = True

            self.dispatch({ 'name': 'subscribe', 'event': event, 'selector': selector, 'capture': capture, 'key': str(id(callback)) })


    def dispatch(self, command):
        self.protocol.sendMessage(bytes(json.dumps(command), 'utf-8'), False)

    @asyncio.coroutine
    def process(self, protocol, event):
        self.protocol = protocol
        eventtype = event['event']

        if eventtype in self.handlers:
            # Check for local handler
            if 'key' in event:
                key = event['key']

                if key in self.handlers[eventtype]:
                    for handler in self.handlers[eventtype][key]:
                        if callable(handler):
                            command = yield from handler(event, self)

                            if command:
                                self.dispatch(command)

            # Check for global handler
            for handler in self.handlers[eventtype]['_']:
                if callable(handler):
                    command = yield from handler(event, self)

                    if command:
                        self.dispatch(command)


class SofiEventProtocol(WebSocketServerProtocol):
    """Websocket event handler which dispatches events to SofiEventProcessor"""

    def onConnect(self, request):
        print("Client connecting: %s" % request.peer)

    def onOpen(self):
        print("WebSocket connection open")

    @asyncio.coroutine
    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf-8')))
            body = json.loads(payload.decode('utf-8'))

            if 'event' in body:
                yield from self.processor.process(self, body)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))
        exit(0)


class SofiEventServer(object):
    """Websocket event server"""

    def __init__(self, hostname=u"127.0.0.1", port=9000, processor=None):

        self.hostname = hostname
        self.port = port
        self.processor = processor

        factory = WebSocketServerFactory(u"ws://" + hostname + u":" + str(port))
        protocol = SofiEventProtocol
        protocol.processor = processor
        protocol.app = self

        factory.protocol = protocol

        self.loop = asyncio.get_event_loop()
        self.server = self.loop.create_server(factory, '0.0.0.0', port)

    def start(self):
        self.loop.run_until_complete(self.server)

        try:
            path = os.path.dirname(os.path.realpath(__file__))
            webbrowser.open('file:///' + os.path.join(path, 'main.html'))
            self.loop.run_forever()

        except KeyboardInterrupt:
            pass

        finally:
            self.server.close()
            self.loop.close()

    def __repr__(self):
        return "<EventServer(%s, %s)>" % (self.hostname, self.port)

    def __str__(self):
        return repr(self)
