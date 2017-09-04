import asyncio
import os, sys
import subprocess

import json
import webbrowser
import logging

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol
from autobahn.websocket.types import ConnectionDeny


class SofiEventProtocol(WebSocketServerProtocol):
    """WebSocket / UI event handler instantiated for each connection"""

    def onConnect(self, request):
        """Triggered when a new WebSocket client (UI layer) attempts to connect"""

        logging.info("Client connecting: %s" % request.peer)

        if self.app.singleclient and len(self.app.clients) == 1:
            logging.info("Running in Single client mode - extra connection request rejected")
            raise ConnectionDeny(403)

        self.app.clients.append(self)

    def onOpen(self):
        """Triggered when a connection is established"""

        logging.info("WebSocket connection open")

    async def onMessage(self, payload, isBinary):
        """Called whenever a new message is received"""

        if isBinary:
            logging.info("Binary message received: {} bytes".format(len(payload)))
        else:
            logging.info("Text message received: {}".format(payload.decode('utf-8')))
            body = json.loads(payload.decode('utf-8'))

            if 'event' in body:
                await self.app.process(self, body)
                return

    def onClose(self, wasClean, code, reason):
        """Called when the client closes the connection"""

        logging.info("WebSocket connection closed: {}".format(reason))

        # Exit the application if only listening to one client
        if self.app.singleclient and self.app.clients[0] == self:
            # TODO: This should probably be cleaner
            exit(0)

    def dispatch(self, command):
        """Send a command to the client / UI layer"""

        self.sendMessage(bytes(json.dumps(command), 'utf-8'), False)


class Sofi():

    def __init__(self, singleclient=True, hostname="127.0.0.1", address="0.0.0.0", port=9000, protocol=SofiEventProtocol):
        # General application configuration info
        self.hostname = hostname
        self.address = address
        self.port = port

        # Protocol class that will manage messaging
        self.protocol = protocol
        protocol.app = self

        # Event handlers
        self.handlers = {
            'init': {'_': set()},
            'load': {'_': set()},
            'close': {'_': set()},
            'click': {'_': set()},
            'mousedown': {'_': set()},
            'mouseup': {'_': set()},
            'keydown': {'_': set()},
            'keyup': {'_': set()},
            'keypress': {'_': set()}
        }

        # Client management
        self.clients = list()
        self.singleclient = singleclient

        # Create the factory that generates protocols to handle socket communications
        factory = WebSocketServerFactory("ws://" + hostname + ":" + str(port))
        factory.protocol = protocol

        # Create the Asyncio event loop
        self.loop = asyncio.get_event_loop()

        # Create the loop server
        self.server = self.loop.create_server(factory, address, port)

    def start(self, desktop=True, browser=True):
        """Start the application"""

        self.loop.run_until_complete(self.server)

        try:
            # Automatically open the browser if requested
            if desktop:
                if browser:
                    # path = os.path.dirname(os.path.realpath(__file__))
                    if getattr(sys, 'frozen', False):
                        # we are running in a bundle
                        path = sys._MEIPASS
                        webbrowser.open('file:///' + os.path.join(path, 'sofi/app/main.html'))
                    else:
                        # we are running in a normal Python environment
                        path = os.path.dirname(os.path.realpath(__file__))
                        webbrowser.open('file:///' + os.path.join(path, 'main.html'))
                else:
                    if getattr(sys, 'frozen', False):
                        # we are running in a bundle
                        path = sys._MEIPASS
                        if sys.platform == 'linux':
                            pass
                        elif sys.platform == 'windows':
                            pass
                        else:
                            # Assume Mac
                            subprocess.Popen([os.path.join(path, 'browser.app/Contents/MacOS/cefsimple'),
                                              '--url=file://' + os.path.join(path, 'sofi/app/main.html')])
                    else:
                        # we are running in a normal Python environment
                        path = os.path.dirname(os.path.realpath(__file__))
                        if sys.platform == 'linux':
                            pass
                        elif sys.platform == 'windows':
                            pass
                        else:
                            # Assume Mac
                            subprocess.Popen([os.path.join(path, '../../browser.app/Contents/MacOS/cefsimple'),
                                              '--url=file:///' + os.path.join(path, 'main.html')])


            # Start listening for connections
            self.loop.run_forever()

        except KeyboardInterrupt:
            logging.info("Keyboard Interrupt received.")

            # Tell any clients that we're closing
            for client in self.clients:
                client.sendClose()
                pass

            self.server.close()

        finally:
            # Gather any remaining tasks so we can cancel them
            asyncio.gather(*asyncio.Task.all_tasks()).cancel()
            self.loop.stop()

            logging.info("Cancelling pending tasks...")
            self.loop.run_forever()

            logging.info("Stopping Server...")
            self.loop.close()

    def register(self, event, callback, selector=None, client=None):
        """Register an event callback"""

        # If we didn't know of this event, add it to the handler mappings
        if event not in self.handlers:
            self.handlers[event] = {'_': set()}

        capture = False
        if selector is None:
            key = '_'
            selector = 'html'
            capture = True
        else:
            key = str(id(callback)) + selector

        if key not in self.handlers[event]:
            self.handlers[event][key] = set()

        self.handlers[event][key].add(callback)

        if event not in ('init', 'load', 'close') and len(self.handlers[event].keys()) > 1:
            if self.singleclient or client is None:
                client = self.clients[0]

            # Tell the UI layer to subscribe to this event
            client.dispatch({'name': 'subscribe', 'event': event, 'selector': selector, 'capture': capture, 'key': str(id(callback)) + selector})

    def unregister(self, event, callback, selector=None, client=None):
        """Remove an event callback"""

        if event not in self.handlers:
            return

        if selector is None:
            self.handlers[event]['_'].remove(callback)
        else:
            handler_list = self.handlers[event].get(str(id(callback)) + selector, set())
            if callback in handler_list:
                handler_list.remove(callback)

        if event not in ('init', 'load', 'close'):
            if self.singleclient or client is None:
                client = self.clients[0]

            # Tell the UI layer to unsubscribe from this event
            client.dispatch({'name': 'unsubscribe', 'event': event, 'selector': selector, 'key': str(id(callback)) + selector})

    def dispatch(self, command):
        """Send a command to the UI layer. Only use in singleclient mode"""

        if self.singleclient:
            self.clients[0].dispatch(command)
        else:
            raise NotImplementedError("Using Sofi.dispatch with more than one client can have unintended consequences and is not supported")

    async def process(self, protocol, event):
        """Process a new event"""

        eventtype = event['event']
        event['client'] = protocol

        if eventtype in self.handlers:
            # Check for local handler
            if 'key' in event:
                key = event['key']

                if key in self.handlers[eventtype]:
                    for handler in list(self.handlers[eventtype][key]):
                        if callable(handler):
                            await handler(event)

            # Check for global handler
            for handler in list(self.handlers[eventtype]['_']):
                if callable(handler):
                    await handler(event)

    def load(self, html, client=None):
        """Initialize the UI. This will replace the document <html> tag contents with the supplied html."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'init', 'html': html})

    def append(self, selector, html, client=None):
        """Append the given html to all elements matching this selector"""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'append', 'selector': selector, 'html': html})

    def remove(self, selector, client=None):
        """Remove the elements matching this selector."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'remove', 'selector': selector})

    def replace(self, selector, html, client=None):
        """Replace the contents all elements matching this selector with the given html."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'replace', 'selector': selector, 'html': html})

    def addclass(self, selector, cl, client=None):
        """Add the given class from all elements matching this selector."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'addclass', 'selector': selector, 'cl': cl})

    def removeclass(self, selector, cl, client=None):
        """Remove the given class from all elements matching this selector."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'removeclass', 'selector': selector, 'cl': cl})

    def text(self, selector, text, client=None):
        """Set the text for elements matching the selector."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'text', 'selector': selector, 'text': text})

    def attr(self, selector, attr, value, client=None):
        """Set the attribute for elements matching this selector."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'attr', 'selector': selector, 'attr': attr, 'value': value})

    def style(self, selector, style, value, priority=None, client=None):
        """Set the style for elements matching this selector. The priority field can be set to "important" to force the style."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'style', 'selector': selector, 'style': style, 'value': value, 'priority': priority})

    def property(self, selector, property, value, client=None):
        """Set the property for elements matching this selector. Properties are special attributes like 'checked' or 'value'."""

        if client is None:
            client = self.clients[0]

        client.dispatch({'name': 'attr', 'selector': selector, 'property': property, 'value': value})
