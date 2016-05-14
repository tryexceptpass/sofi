from sofi.app import SofiEventServer, SofiEventProcessor
from sofi import Container, View, Row
from sofi import Paragraph, Heading, Anchor
from sofi import Navbar, Dropdown, DropdownItem
from sofi import Button, ButtonGroup, ButtonToolbar

import asyncio
import json
import time

@asyncio.coroutine
def main(protocol):
    print("MAIN")
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
    btnP = Button("Primary", "primary")
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

    v.addelement(c)

    return { 'name': 'init', 'html': str(v) }

@asyncio.coroutine
def load(protocol):
    print("LOADED")

    yield from asyncio.sleep(5)

    for i in range(1, 5):
        protocol.dispatch({'name': 'style', 'selector': '#fiddle', 'style': 'font-size', 'value': str(i*2) + 'em', 'priority': 'important'})
        yield from asyncio.sleep(1)

    yield from asyncio.sleep(5)

    protocol.dispatch({'name': 'remove', 'selector': '#fiddle'})

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
