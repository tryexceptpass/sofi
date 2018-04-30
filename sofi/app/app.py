import asyncio
import os
import sys
import shutil
import subprocess

import json
import webbrowser
import logging

from sofi.ui import Element

import websockets
from threading import Thread


class Sofi():

    def __init__(self, singleclient=True, background=False, hostname="127.0.0.1", address="0.0.0.0", port=9000):
        # General application configuration info
        self.hostname = hostname
        self.address = address
        self.port = port
        self.background = background
        self.thread = None

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

        if self.background:
            # Make a new asyncio event loop
            self.loop = asyncio.new_event_loop()

            # Make a background thread that sets up the loop
            self.thread = Thread(target=self.__run_loop)

        else:
            # Get the current asyncio event loop
            self.loop = asyncio.get_event_loop()

    def __run_loop(self):
        # Set event loop
        if self.background:
            logging.info("Running in background")
            asyncio.set_event_loop(self.loop)

        # Create the loop server
        self.server = self.loop.run_until_complete(websockets.serve(self.handler, self.address, self.port))

        try:
            logging.info("Starting server")
            self.loop.run_forever()

        except KeyboardInterrupt:
            logging.info("Keyboard Interrupt received.")

        finally:
            # Tell any clients that we're closing
            self.server.close()
            self.loop.run_until_complete(asyncio.sleep(0.1))

            # Gather any remaining tasks so we can cancel them
            asyncio.gather(*asyncio.Task.all_tasks()).cancel()
            self.loop.stop()

            logging.info("Cancelling pending tasks...")
            self.loop.run_forever()

            logging.info("Stopping Server...")
            self.loop.close()

    async def handler(self, websocket, path):
        """Called whenever a new message is received"""

        if self.singleclient and len(self.clients) == 1:
            websocket.close(reason="Only one client allowed in single-client mode.")

        self.clients.append(websocket)
        logging.info(f"New client connected from {websocket.remote_address}")

        async for msg in websocket:
            try:
                logging.info(f"Message received: {msg}")
                body = json.loads(msg)

                if 'event' in body:
                    await self.process(websocket, body)

            except Exception as e:
                logging.exception(f"Exception when handling message {msg} from client {websocket.remote_address}")

        self.clients.remove(websocket)

    def dispatch(self, command, client=None):
        """Send a command to the UI layer"""

        command = json.dumps(command)
        if self.singleclient:
            # asyncio.gather(self.clients[0].send(command), loop=self.loop)
            asyncio.run_coroutine_threadsafe(self.clients[0].send(command), self.loop)

        else:
            if client is None:
                asyncio.run_coroutine_threadsafe(asyncio.gather(*[c.send(command) for c in self.clients], loop=self.loop))
            else:
                # asyncio.gather(client.send(command), loop=self.loop)
                asyncio.run_coroutine_threadsafe(client.send(command), self.loop)

    def start(self, desktop=True, browser=True):
        """Start the application"""

        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            path = sys._MEIPASS
        else:
            path = os.path.dirname(os.path.realpath(__file__))

        # Automatically open the browser if requested
        if desktop:
            if browser:
                if getattr(sys, 'frozen', False):
                    # we are running in a bundle
                    webbrowser.open('file:///' + os.path.join(path, 'sofi/app/main.html'))
                else:
                    # we are running in a normal Python environment
                    webbrowser.open('file:///' + os.path.join(path, 'main.html'))
            else:
                if getattr(sys, 'frozen', False):
                    # we are running in a bundle
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
                    if sys.platform == 'linux':
                        pass
                    elif sys.platform == 'windows':
                        pass
                    else:
                        # Assume Mac
                        subprocess.Popen([os.path.join(path, '../../browser.app/Contents/MacOS/cefsimple'),
                        '--url=file:///' + os.path.join(path, 'main.html')])

        with open(os.path.join(path, '_sofi.js'), 'rb') as source:
            jsfile = os.path.join(path, 'sofi.js')

            if os.path.exists(jsfile):
                os.remove(jsfile)

            with open(jsfile, 'wb') as f:
                f.write(bytes('var SOCKET_URL = "ws://' + self.hostname + ":" + str(self.port) + '/"\n', 'utf-8'))
                shutil.copyfileobj(source, f)

        if self.background:
            self.thread.start()

        else:
            self.__run_loop()

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
            # Tell the UI layer to subscribe to this event
            self.dispatch({'name': 'subscribe', 'event': event, 'selector': selector, 'capture': capture, 'key': str(id(callback)) + selector}, client)

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
            # Tell the UI layer to unsubscribe from this event
            self.dispatch({'name': 'unsubscribe', 'event': event, 'selector': selector, 'key': str(id(callback)) + selector}, client)

    async def process(self, client, event):
        """Process a new event"""

        eventtype = event['event']
        event['client'] = client

        if eventtype in self.handlers:
            # Check for local handler
            if 'key' in event:
                key = event['key']

                if key in self.handlers[eventtype]:
                    for handler in list(self.handlers[eventtype][key]):
                        if callable(handler):
                            asyncio.run_coroutine_threadsafe(handler(event), self.loop)

            # Check for global handler
            for handler in list(self.handlers[eventtype]['_']):
                if callable(handler):
                    asyncio.run_coroutine_threadsafe(handler(event), self.loop)

    def load(self, html, client=None):
        """Initialize the UI. This will replace the document <html> tag contents with the supplied html."""

        if isinstance(html, Element):
            html = str(html)

        self.dispatch({'name': 'init', 'html': html}, client)

    def append(self, selector, html, client=None):
        """Append the given html to all elements matching this selector"""

        if isinstance(html, Element):
            html = str(html)

        self.dispatch({'name': 'append', 'selector': selector, 'html': html}, client)

    def remove(self, selector, client=None):
        """Remove the elements matching this selector."""

        self.dispatch({'name': 'remove', 'selector': selector}, client)

    def replace(self, selector, html, client=None):
        """Replace the contents all elements matching this selector with the given html."""

        if isinstance(html, Element):
            html = str(html)

        self.dispatch({'name': 'replace', 'selector': selector, 'html': html}, client)

    def addclass(self, selector, cl, client=None):
        """Add the given class from all elements matching this selector."""

        self.dispatch({'name': 'addclass', 'selector': selector, 'cl': cl}, client)

    def removeclass(self, selector, cl, client=None):
        """Remove the given class from all elements matching this selector."""

        self.dispatch({'name': 'removeclass', 'selector': selector, 'cl': cl}, client)

    def text(self, selector, text, client=None):
        """Set the text for elements matching the selector."""

        self.dispatch({'name': 'text', 'selector': selector, 'text': text}, client)

    def attr(self, selector, attr, value, client=None):
        """Set the attribute for elements matching this selector."""

        self.dispatch({'name': 'attr', 'selector': selector, 'attr': attr, 'value': value}, client)

    def style(self, selector, style, value, priority=None, client=None):
        """Set the style for elements matching this selector. The priority field can be set to "important" to force the style."""

        self.dispatch({'name': 'style', 'selector': selector, 'style': style, 'value': value, 'priority': priority}, client)

    def prop(self, selector, property, value, client=None):
        """Set the property for elements matching this selector. Properties are special attributes like 'checked' or 'value'."""

        self.dispatch({'name': 'attr', 'selector': selector, 'property': property, 'value': value}, client)
