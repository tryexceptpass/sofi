from sofi.app import SofiEventServer, SofiEventProcessor
from sofi import Container, Paragraph, Heading, View, Navbar

import asyncio
import json
import time

@asyncio.coroutine
def main(protocol):
   print("MAIN")
   v = View()

   c = Container()
   n = Navbar(brand="SOFI", fixed='top')
   n.addlink("LINK 1")
   n.addlink("LINK 2")
   n.addlink("LINK 2", active=True)
   c.additem(n)
   #c.additem(Heading(2, "Dude!"))
   #c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   return { 'name': 'init', 'html': str(v) }

@asyncio.coroutine
def load(protocol):
   print("LOADED")

   yield from asyncio.sleep(5)

   for i in range(1, 5):
      protocol.dispatch({'name': 'style', 'selector': 'p', 'style': 'font-size', 'value': str(i*2) + 'em', 'priority': 'important'})
      yield from asyncio.sleep(1)

   yield from asyncio.sleep(5)

   protocol.dispatch({'name': 'remove', 'selector': 'p'})

   msg = 'SWEET!!!'
   for i in range(8):
      protocol.dispatch({ 'name': 'text', 'selector': 'h2', 'text': msg[:i]})
      yield from asyncio.sleep(1)

   return


sep = SofiEventProcessor()
sep.register('init', main)
sep.register('load', load)

app = SofiEventServer(processor=sep)
app.start()