from sofi.app import SofiEventServer, SofiEventProcessor

from sofi import Container, Paragraph, Heading, View

import json

def main(socket):
   v = View()

   c = Container()
   c.additem(Heading(2, "Dude!"))
   c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   return str(v)



sep = SofiEventProcessor()
sep.oninit = main


app = SofiEventServer(processor=sep)
app.start()