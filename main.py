import os
from flask import Flask, request
from slackclient import SlackClient
from pprint import pprint
import json

with open('./api_tokens.json') as data_file:
    token = json.load(data_file)['token']

pprint(token)

scope = "read"

sc = SlackClient(token)

# sc.api_call(
#   "chat.postMessage",
#   channel="#general",
#   text="Hello from Python! :tada:"
# )

channel_list = sc.api_call(
                      "channels.list",
                      types="private_channel",
                      scope="read")

# pprint([c['is_private'] for c in channel_list['channels']])
pprint(channel_list)


# sc.api_call(
#   "channels.info",
#   channel=""
# )
