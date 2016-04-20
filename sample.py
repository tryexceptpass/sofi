from sofi.app import SofiEventServer, SofiEventProcessor
from sofi import Container, Paragraph, Heading, View, Navbar, Dropdown, DropdownItem

import asyncio
import json
import time

@asyncio.coroutine
def main(protocol):
    print("MAIN")
    v = View()
   
    c = Container()
    n = Navbar(brand="SOFI", fixed='top')
    n.addnavlink("LINK 1")
    n.addnavlink("LINK 2")
    n.addnavlink("LINK 2", active=True)
    
    b = Dropdown("Dropdown", align='right')
    b.addelement(DropdownItem('Item Header', header=True))
    b.addelement(DropdownItem('Item 1'))
    b.addelement(DropdownItem('Item 2', disabled=True))
    b.addelement(DropdownItem('', divider=True))
    b.addelement(DropdownItem('Item 3'))
    
    c.addelement(n)
     
    c.addelement(Heading(2, "Dude!"))
    c.addelement(Paragraph("Where's My Car?"))
   
    c.addelement(b)
    
    v.addelement(c)
   
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