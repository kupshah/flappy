import os
import json
import sys
#import networkx
#import requests
#from bottle import route, run, post, request, app
import random
from urllib.parse import urlencode
from urllib.request import Requests, urlopen
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()
    if data['name'] != 'flappy-bot':
        msg = "This is a new test message, {} \n This is a reply to '{}'".format(data['name'],data["text"])
        
        send_message(msg)

        return "ok",200

def send_message(msg):
    url = "https://api.groupme.com/v3/bots/post"
    bot_id = '288f9e18900355d4b59ec6f717'
    
    data = {"bot_id" : bot_id, "text" : msg}
    request = Request(url,urlencode(data).encode())
    json = urlopen(request).read().decode()
        










    
