from sofi.app import Sofi
from sofi.ui import Container, View, Row, Panel, Column
from sofi.ui import Paragraph, Heading, Anchor, Image
from sofi.ui import Navbar, Dropdown, DropdownItem
from sofi.ui import Button, ButtonGroup, ButtonToolbar, ButtonDropdown

import asyncio
import json
import time

import logging
import os


async def oninit(event):
    logging.info("INIT")
    v = View("Sample Sofi Widget Application")

    n = Navbar(brand="SOFI", fixed='top')
    n.addlink("LINK 1")
    n.addlink("LINK 2")
    n.addtext("Just some Text with a " + str(Anchor("link", cl='navbar-link')))
    n.addlink("LINK 2", active=True)

    b = Dropdown("Dropdown", align='right')
    b.addelement(DropdownItem('Item Header', header=True))
    b.addelement(DropdownItem('Item 1'))
    b.addelement(DropdownItem('Item 2', disabled=True))
    b.addelement(DropdownItem('', divider=True))
    b.addelement(DropdownItem('Item 3'))

    n.adddropdown(b)

    v.addelement(n)

    c = Container()
    tb = ButtonToolbar()
    bgrp = ButtonGroup()
    btnDe = Button("Default")
    btnP = Button("Primary", "primary", ident='primary')
    btnI = Button("Info", "info")
    bgrp2 = ButtonGroup()
    btnS = Button("Success", "success", ident='secondary')
    btnW = Button("Warning", "warning")
    btnDa = Button("Danger", "danger")

    r = Row()
    bgrp.addelement(btnDe)
    bgrp.addelement(btnP)
    bgrp.addelement(btnI)
    bgrp2.addelement(btnS)
    bgrp2.addelement(btnW)
    bgrp2.addelement(btnDa)
    tb.addelement(bgrp)
    tb.addelement(bgrp2)
    r.addelement(tb)
    c.addelement(r)

    c.newrow(Heading(2, "Dude!"))
    c.newrow(Paragraph("Where's My Car?", ident="fiddle"))

    bd = ButtonDropdown('A Dropdown', size='xs', dropup=True, split=True, severity="success")
    bd.addelement(DropdownItem('Item Header', header=True))
    bd.addelement(DropdownItem('Item 1'))
    bd.addelement(DropdownItem('Item 2', disabled=True))
    bd.addelement(DropdownItem('', divider=True))
    bd.addelement(DropdownItem('Item 3'))
    c.newrow(bd)

    r = Row()
    col = Column(count=3)
    p = Panel("Panel 1")
    col.addelement(p)
    r.addelement(col)

    col = Column(count=3)
    p = Panel("Panel 2", 'danger')
    col.addelement(p)
    r.addelement(col)

    c.newrow(Paragraph())
    c.addelement(r)

    v.addelement(c)

    app.load(str(v), event['client'])


async def onload(event):
    logging.info("LOADED")

    app.register('click', buttonclicked, selector='#primary', client=event['client'])
    app.register('click', buttonclicked, selector='#secondary', client=event['client'])
    app.register('click', buttonclicked, selector='#secondary', client=event['client'])

    await asyncio.sleep(5)

    text = await app.gettext('#primary', event['client'])
    attr = await app.getattribute('#primary', 'class', event['client'])
    prop = await app.getproperty('#primary', 'type', event['client'])

    logging.info(f"TEXT {text}, ATTR {attr}, PROP {prop}")

    for i in range(1, 5):
        app.style("#fiddle", 'font-size', str(i*2) + "em", 'important', event['client'])

        await asyncio.sleep(1)

    await asyncio.sleep(5)

    img = Image()
    img.datauri(os.path.join(os.path.dirname(__file__), 'test', 'test.png'))

    app.replace("#fiddle", str(img), event['client'])

    msg = 'SWEET!!!'
    for i in range(8):
        app.set_text("h2", msg[:i], event['client'])
        await asyncio.sleep(1)


async def clicked(event):
    logging.info("CLICKED!")


async def buttonclicked(event):
    if ('id' in event['event_object']['target']):
        logging.info("BUTTON " + event['event_object']['target']['id'] + " CLICKED!")
    else:
        logging.info("BUTTON " + event['event_object']['target']['innerText'] + " CLICKED!")

    app.unregister('click', buttonclicked, selector='#' + event['event_object']['target']['id'], client=event['client'])


logging.basicConfig(format="%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s", level=logging.INFO)

app = Sofi(singleclient=True)
app.register('init', oninit)
app.register('load', onload)

# app.start()
app.start()
