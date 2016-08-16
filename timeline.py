from sofi.app import Sofi
from sofi import Container, View, Row, Column
from sofi import Panel, Paragraph

import asyncio
import json
import time

import tweepy
from datetime import datetime


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tue Jun 07 23:05:55 +0000 2016
dateformat = "%a %b %d %H:%M:%S %z %Y"

@asyncio.coroutine
def main(event, interface):
    print("MAIN")
    v = View()
    c = Container()

    tweets = api.home_timeline()

    for tweet in tweets:
        p = Panel(heading=True, style="max-height:150px;min-height:150px;")
        p.setheading(tweet.user.screen_name + "<div class='pull-right'>" + tweet.created_at.strftime("%b %d %Y %H:%M:%S") + "</div>")
        p.addelement(Paragraph(tweet.text))
        col = Column('md', 4)
        col.addelement(p)
        c.addelement(col)

    v.addelement(c)

    return { 'name': 'init', 'html': str(v) }

@asyncio.coroutine
def load(event, interface):
    print("LOADED")

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

    return


app = Sofi()
app.register('init', main)
app.register('load', load)

app.start()
