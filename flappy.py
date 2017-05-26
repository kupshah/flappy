import os
import json
import requests
from bottle import route, run, post, request, app
import random
import markovify

#consumerkey = 'Z7LKSpDccQBM1XjYaHUbA3wPS'
#consumersecret = 'G3fnqzLXWkbAaR1AXj3PVhKZ2OTqWi0n2gpS1QTgTpV8vu33w4'
#accesstoken = '763227243795578880-um4Mn9fvrOxYksSO7hNb8CRKmNUuzlj'
#accesstokensecret='umYFYl1QOERnzs2BYpm9TYWWkLsnGnICdxGecbpxHpVJI'
#
#kanye = '169686021'
#vasu = '959202876'
#
#api = twitter.Api(consumer_key=consumerkey, consumer_secret=consumersecret, access_token_key=accesstoken, access_token_secret=accesstokensecret)
#
#def get_tweets(user):
#    user_id = user
#    tweets=[]    
#    maxid = 0
#    while True:
#        statuses = api.GetUserTimeline(user_id, count=200, max_id=maxid)
#        if not (len(statuses)-1):
#            break
#        for i in range(len(statuses)):
#            if i == (len(statuses)-1):
#                maxid = statuses[i].id + 1
#            tweets = tweets + [statuses[i].text]
#            
#    return tweets
#    
#kanye_tweets = get_tweets(kanye)
#numkt = len(kanye_tweets)-1
#
#vasu_tweets = get_tweets(vasu)
#numvt = len(vasu_tweets)-1

#@post('/')
#def botty():
#    data = request.json
#    print data['text']
#    print data['sender_id']
#    if data['text'] and data['sender_id']!='352844':
#        text = data['text']
#        
#        text = text.lower()
#        i = 0
#        words = text.split()
#        for w in words:
#            if 'fuck' in w:
#                i = i+1
#            elif 'ass' in w:
#                i =i+1
#            elif 'bitch' in w:
#                i =i+1
#            elif 'shit' in w:
#                i = i+1 
#            elif 'cunt' in w:
#                i = i+1  
#        if i>4:
#            message = {'bot_id':'0be9e789d8cb81f22caa963a29', 'text':'WATCH YO PROFAMITY', 'attachments':[{'type':'image', 'url':'https://i.groupme.com/480x360.jpeg.4184aba9e57e4e13b88333bf4fe10a65'}] }
#            message = json.dumps(message)
#            r = requests.post('https://api.groupme.com/v3/bots/post', message) 
#        i = 0
#                        
#        if text == 'andrew you are a fucking idiot.':
#            message = {'bot_id':'0be9e789d8cb81f22caa963a29', 'text':'Hell yeah he is'}
#            message = json.dumps(message)
#            r = requests.post('https://api.groupme.com/v3/bots/post', message)
#            
#        for w in words:
#            if 'botty' in w:
#                i = i+1
#            elif 'give' in w:
#                i =i+1
#            elif 'kanye' in w:
#                i =i+1
#        if i>2:
#            kt_num = random.randrange(0, (numkt))
#            message = {'bot_id':'0be9e789d8cb81f22caa963a29', 'text':kanye_tweets[kt_num]}
#            message = json.dumps(message)
#            r = requests.post('https://api.groupme.com/v3/bots/post', message) 
#        i = 0
#
#        for w in words:
#            if 'botty' in w:
#                i = i+1
#            elif 'give' in w:
#                i =i+1
#            elif 'vasu' in w:
#                i =i+1
#        if i>2:
#            vt_num = random.randrange(0, (numvt))
#            message = {'bot_id':'0be9e789d8cb81f22caa963a29', 'text':vasu_tweets[vt_num]}
#            message = json.dumps(message)
#            r = requests.post('https://api.groupme.com/v3/bots/post', message) 
#        i = 0

with open('bot_messages.txt', 'r') as f:
    messages = f.read()
msg_model = markovify.Text(messages)

@post('/')
def flappy():
    
    data = request.json
    print data['text']
    print data['sender_id']
    if data['text']:
        text = data['text']
        text = text.lower()
        k = 5
        i = 35
        a = 49
        v = 15
        s = 99
        words = text.split()
        if 'kunaal' in words:
            if k == random.randint(2,6):      
                message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':random.choice("kunaal is gr8", "I <3 Kunaal", "Kunaal is my creator and i love him so much not cause he can destroy m ebut cause he's great",
                                                                                   "no one amazing like kunaal", "So cool kunaal is",
                                                                                   "Kunaal is like 1000x cooler than amani lol hes the best",
                                                                                   "i love my creator qunol", "I h8 everyone except kunaal",
                                                                                   "Kunaal kunaal kunaal kunaal kunaal kunaal so amazing",
                                                                                   "i h8 kunaal")}
                r = requests.post('https://api.groupme.com/v3/bots/post', message)
                
        if 'flappy' in words:
            message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':msg_model.make_short_sentence(140)}
            message = json.dumps(message)
            r = requests.post('https://api.groupme.com/v3/bots/post', message)

        if len(words) > 1:
            if i == random.randint(20,50):
                message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':msg_model.make_short_sentence(140)}
                message = json.dumps(message)
                r = requests.post('https://api.groupme.com/v3/bots/post', message)

        if "amani" in words or "amangi" in words:
            if a == random.randint(42,50):
                message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':random.choice("ha amani sux", "I hate amangi :)",
                                                                                       "amani is the #1 worst responder",
                                                                                       "Ben franklin texts back faster than Amani",
                                                                                       "Why is anyone friends with amani", "Amani is pretty cool",
                                                                                       "maybe some people could consider amani as being okay",
                                                                                       "amani ew")}
                message = json.dumps(message)
                r = requests.post('https://api.groupme.com/v3/bots/post', message)

        if "vasu" in words:
            if v == 15:
                message_to_send = random.choice("vasu is sooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo dumb",
                                                                                   "vasu stupidest smrt person in the world.... HOWW??W?W??W??",
                                                                                   "vasu is less cool than kunaal",
                                                                                   "kanye sucks roflmao",
                                                                                   "i can see the future and i'll tell you.. Vasu will die soon")
                
                message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':message_to_send}
                message = json.dumps(message)
                r = requests.post('https://api.groupme.com/v3/bots/post', message)

        if "soap" in words or "shloak" in words:
            if s == random.randomint(90,100):
                message = {'bot_id':'288f9e18900355d4b59ec6f717', 'text':random.choice("shloak is ok",
                                                                                       "how does that guy have friends?",
                                                                                       "shloak lame",
                                                                                       "shloak needs peer pressure to do more drugs",
                                                                                       "wil soapy all grown up now",
                                                                                       "i am a sad robot")}
                
                                                                                       
            
                                                                                   
                                                                                   
            





run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
