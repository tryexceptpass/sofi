from sofi.app import Sofi
from sofi.ui import Container, View, Row, Column
from sofi.ui import Panel, Paragraph

import asyncio
import json

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


async def main(event):
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

    app.load(str(v))


app = Sofi()
app.register('init', main)

app.start()
