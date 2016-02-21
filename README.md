## Overview
`sofi` is an OS agnostic UI module for Python.

The main idea is to allow rapid, pythonic GUI development using standard web-based widgets from `bootstrap` and
other common HTML5 libraries and package them in such a way that all event processing is done within python using
`websockets`.

We're in an **alpha** stage of development, still getting most of the main APIs in place.

## Usage
The `SofiEventServer` runs the main event thread with `.start()` and the `SofiEventProcessor` is where all the event
handling is done.

Following basic practices from bootstrap, the widgets should be within a `Container`. The main page is represented with
the `View` class.

```python
from sofi.app import SofiEventServer, SofiEventProcessor

from sofi import Container, Paragraph, Heading, View

import json

def main(socket):
   v = View()

   c = Container()
   c.additem(Heading(2, "Dude!"))
   c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   socket.sendMessage(bytes(json.dumps({'html': str(v)}), 'utf-8'), False)



sep = SofiEventProcessor()
sep.oninit = main

app = SofiEventServer(processor=sep)
app.start()
```
