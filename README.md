[![Stories in Ready](https://badge.waffle.io/tryexceptpass/sofi.png?label=ready&title=Ready)](https://waffle.io/tryexceptpass/sofi)
## Overview
`sofi` is an OS agnostic UI module for Python.

The main idea is to allow rapid, pythonic GUI development using standard web-based widgets from `bootstrap` and
other common HTML5 libraries and package them in such a way that all event processing is done within python using
`websockets`.

We're in an **alpha** stage of development, still getting most of the main APIs in place.

## Usage
The `sofi.app.Sofi` object runs the main event thread with `.start()` and provides the `register` function for adding event subscriptions.

Following basic practices from bootstrap, the widgets should be within a `Container`. The main page is represented with the `View` class.

Below is a quick idea of how to get things going, but check out `sample.py` for a more complicated hello world which instantiates a navbar item, adds a few links, creates some buttons, registers events and performs some timed updates.

**Note:** I understand that some of the return values from the event processors are not user friendly. I'll wrap those up into something pretty in the near future.

```python
from sofi.app import Sofi
from sofi import Container, Paragraph, Heading, View

import json
import asyncio

@asyncio.coroutine
def main(event, interface)):
   v = View()

   c = Container()
   c.additem(Heading(2, "Dude!"))
   c.additem(Paragraph("Where's My Car?"))

   v.additem(c)

   return { 'name': 'init', 'html': str(v) }


# Instantiate the application
app = Sofi()

# Register the main event handler
app.register('init', main)

# Start the app (opens the default browser) and listen for events
app.start()
```

## What do the widgets look like?

![sample.py](https://cdn-images-1.medium.com/max/800/1*euug6f885sjtRPOMt_Vc6g.png)

![timeline.py](https://cdn-images-1.medium.com/max/800/1*AmbFclbXWFdIRYbpa0cyBw.png)
