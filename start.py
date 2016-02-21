from sofi.app import SofiEventServer, SofiEventProcessor

from sofi import Container, Paragraph, Heading, View

import json

def initialize(socket):
   v = View()

   c = Container()
   c.additem(Heading(2, "Dude!"))
   c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   socket.sendMessage(bytes(json.dumps({'html': str(v)}), 'utf-8'), False)



sep = SofiEventProcessor()
sep.oninit = initialize

app = SofiEventServer(processor=sep)
app.start()