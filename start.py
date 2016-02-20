from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol
import asyncio

import json
import webbrowser

from sofi import Container, Paragraph, Heading, View

class Test(WebSocketServerProtocol):

   def onConnect(self, request):
      print("Client connecting: %s" + request.peer)

   def onOpen(self):
      print("WebSocket connection open")

   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {} bytes".format(len(payload)))
      else:
         print("Text message received: {}".format(payload.decode('utf8')))
         body = json.loads(payload.decode('utf8'))

         if 'event' in body:
            processevent(self, body)

   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {}".format(reason))


def processevent(socket, event):
   if event['event'] == 'load_complete':
      v = View()

      c = Container()
      c.additem(Heading(2, "Dude!"))
      c.additem(Paragraph("Where's My Car?"))

      v.additem(c)

      socket.sendMessage(bytes(json.dumps({'html': str(v)}), 'utf-8'), False)


factory = WebSocketServerFactory(u"ws://127.0.0.1:9000", debug=True)
factory.protocol = Test

loop = asyncio.get_event_loop()
coro = loop.create_server(factory, '0.0.0.0', 9000)

server = loop.run_until_complete(coro)

try:
   webbrowser.open('file:///Users/cabkarian/apps/sofi/test.html')
   loop.run_forever()

except KeyboardInterrupt:
   pass

finally:
   server.close()
   loop.close()