from sofi.app import SofiEventServer, SofiEventProcessor
from sofi import Container, Paragraph, Heading, View

import json

def main():
   print("MAIN")
   v = View()

   c = Container()
   c.additem(Heading(2, "Dude!"))
   c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   return { 'name': 'init', 'html': str(v) }

def load():
   print("LOADED")


sep = SofiEventProcessor()
sep.register('init', main)
sep.register('load', load)

app = SofiEventServer(processor=sep)
app.start()