from autobahn.asyncio.websocket import WebSocketServerFactory
import asyncio

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
         self.sendMessage(payload, isBinary)

   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {}".format(reason))

factory = WebSocketServerFactory(u"ws://127.0.0.1:9000", debug=True)
factory.protocol = Test

loop = asyncio.get_event_loop()
coro = loop.create_server(factory, '0.0.0.0', 9000)

server = loop.run_until_complete(coro)

try:
   loop.run_forever()

except KeyboardInterrupt:
   pass

finally:
   server.close()
   loop.close()