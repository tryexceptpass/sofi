import asyncio
import os
import signal

import json
import webbrowser
import logging

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol

class Sofi():
    def __init__(self):
        self.interface = SofiEventProcessor()
        self.server = SofiEventServer(processor=self.interface)

    def start(self, autobrowse=True):
        """Start the application"""

        self.server.start(autobrowse)

    def register(self, event, callback, selector=None):
        """Register event callback"""

        self.interface.register(event, callback, selector)

    def unregister(self, event, callback, selector=None):
        """Register event callback"""

        self.interface.unregister(event, callback, selector)

    def load(self, html, client=None):
        """Initialize the UI. This will replace the document <html> tag contents with the supplied html."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'init', 'html': html })

    def append(self, selector, html, client=None):
        """Append the given html to all elements matching this selector"""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'append', 'selector': selector, 'html': html })

    def remove(self, selector, client=None):
        """Remove the elements matching this selector."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'remove', 'selector': selector })

    def replace(self, selector, html, client=None):
        """Replace the contents all elements matching this selector with the given html."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'replace', 'selector': selector, 'html': html })

    def addclass(self, selector, cl, client=None):
        """Add the given class from all elements matching this selector."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'addclass', 'selector': selector, 'cl': cl })

    def removeclass(self, selector, cl, client=None):
        """Remove the given class from all elements matching this selector."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'removeclass', 'selector': selector, 'cl': cl })

    def text(self, selector, text, client=None):
        """Set the text for elements matching the selector."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'text', 'selector': selector, 'text': text })

    def attr(self, selector, attr, value, client=None):
        """Set the attribute for elements matching this selector."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'attr', 'selector': selector, 'attr': attr, 'value': value })

    def style(self, selector, style, value, priority=None, client=None):
        """Set the style for elements matching this selector. The priority field can be set to "important" to force the style."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'style', 'selector': selector, 'style': style, 'value': value, 'priority': priority })

    def property(self, selector, property, value, client=None):
        """Set the property for elements matching this selector. Properties are special attributes like 'checked' or 'value'."""

        if client is None:
            client = self.interface

        client.dispatch({ 'name': 'attr', 'selector': selector, 'property': property, 'value': value })


class SofiEventProcessor():
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

    def unregister(self, event, callback, selector=None):
        if event not in self.handlers:
            return

        if selector is None:
            self.handlers[event]['_'].remove(callback)
        else:
            handler_list = self.handlers[event].get(str(id(callback)), [])
            if callback in handler_list:
                handler_list.remove(callback)

        if event not in ('init', 'load', 'close'):
            self.dispatch({ 'name': 'unsubscribe', 'event': event, 'selector': selector, 'key': str(id(callback)) })

    def dispatch(self, command):
        self.protocol.dispatch(command)

    async def process(self, protocol, event):
        self.protocol = protocol
        eventtype = event['event']
        event['client'] = protocol

        if eventtype in self.handlers:
            # Check for local handler
            if 'key' in event:
                key = event['key']

                if key in self.handlers[eventtype]:
                    for handler in self.handlers[eventtype][key]:
                        if callable(handler):
                            await handler(event)

            # Check for global handler
            for handler in self.handlers[eventtype]['_']:
                if callable(handler):
                    await handler(event)


class SofiEventProtocol(WebSocketServerProtocol):
    """Websocket event handler which dispatches events to SofiEventProcessor"""

    def onConnect(self, request):
        logging.info("Client connecting: %s" % request.peer)

    def onOpen(self):
        logging.info("WebSocket connection open")

    async def onMessage(self, payload, isBinary):
        if isBinary:
            logging.info("Binary message received: {} bytes".format(len(payload)))
        else:
            logging.info("Text message received: {}".format(payload.decode('utf-8')))
            body = json.loads(payload.decode('utf-8'))

            if 'event' in body:
                await self.processor.process(self, body)
                return

    def onClose(self, wasClean, code, reason):
        logging.info("WebSocket connection closed: {}".format(reason))
        exit(0)

    def dispatch(self, command):
        self.sendMessage(bytes(json.dumps(command), 'utf-8'), False)


class SofiEventServer():
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

    def start(self, autobrowse=True):
        self.loop.run_until_complete(self.server)

        try:
            path = os.path.dirname(os.path.realpath(__file__))
            if autobrowse:
                webbrowser.open('file:///' + os.path.join(path, 'main.html'))
            self.loop.run_forever()

        except KeyboardInterrupt:
            logging.info("Keyboard Interrupt received.")
            self.server.close()

        finally:
            asyncio.gather(*asyncio.Task.all_tasks()).cancel()
            self.loop.stop()
            logging.info("Cancelling pending tasks...")
            self.loop.run_forever()
            logging.info("Stopping Server...")
            self.loop.close()

    def __repr__(self):
        return "<SofiEventServer(%s, %s)>" % (self.hostname, self.port)

    def __str__(self):
        return repr(self)
