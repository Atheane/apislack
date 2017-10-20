import os
from flask import Flask, request
from slackclient import SlackClient
from pprint import pprint
import json
import requests


with open('./api_tokens.json') as data_file:
    credentials = json.load(data_file)

token = credentials['token']

sc = SlackClient(token)

dev_channels = ['bash', 'html-css3']

channel_list = sc.api_call(
                      "conversations.list",
                      types="private_channel",
                      exclude_archived=1
                      )

channels = { c['id']:c['name'] for c in channel_list['channels']}

messages = {}

for (k,v) in channels.items():
  messages[v] = sorted(sc.api_call(
                            "conversations.history",
                             channel=k,
                             limit = 20
                            )['messages'], key= lambda d: d['ts'])


test = [ m['file']['preview'] if 'file' in m else m['text']  \
                     for m in messages['react'] ]
print(test)
