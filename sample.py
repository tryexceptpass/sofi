from sofi.app import Sofi
from sofi.ui import Container, View, Row, Panel, Column
from sofi.ui import Paragraph, Heading, Anchor
from sofi.ui import Navbar, Dropdown, DropdownItem
from sofi.ui import Button, ButtonGroup, ButtonToolbar, ButtonDropdown

import asyncio
import json
import time

import logging

@asyncio.coroutine
def main(event, interface):
    logging.info("MAIN")
    v = View()

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
    btnP = Button("Primary", "primary", ident='clickme')
    btnI = Button("Info", "info")
    bgrp2 = ButtonGroup()
    btnS = Button("Success", "success")
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

    return { 'name': 'init', 'html': str(v) }

@asyncio.coroutine
def load(event, interface):
    logging.info("LOADED")

    app.register('click', buttonclicked, selector='button')

    yield from asyncio.sleep(5)

    for i in range(1, 5):
        interface.dispatch({'name': 'style', 'selector': '#fiddle', 'style': 'font-size', 'value': str(i*2) + 'em', 'priority': 'important'})
        yield from asyncio.sleep(1)

    yield from asyncio.sleep(5)

    interface.dispatch({'name': 'remove', 'selector': '#fiddle'})

    msg = 'SWEET!!!'
    for i in range(8):
        interface.dispatch({ 'name': 'text', 'selector': 'h2', 'text': msg[:i]})
        yield from asyncio.sleep(1)

    app.unregister('click', buttonclicked, selector='button')
    return

@asyncio.coroutine
def clicked(event, interface):
    logging.info("CLICKED!")

@asyncio.coroutine
def buttonclicked(event, interface):
    if ('id' in event['event_object']['target']):
        logging.info("BUTTON " + event['event_object']['target']['id'] + " CLICKED!")
    else:
        logging.info("BUTTON " + event['event_object']['target']['innerText'] + " CLICKED!")

logging.basicConfig(format="%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s", level=logging.INFO)

app = Sofi()
app.register('init', main)
app.register('load', load)
#app.register('click', clicked)

app.start(False)
