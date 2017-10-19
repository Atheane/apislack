import os
from flask import Flask, request
from slackclient import SlackClient
from pprint import pprint

token = os.environ["SLACK_API_TOKEN"]

sc = SlackClient(token)

# sc.api_call(
#   "chat.postMessage",
#   channel="#general",
#   text="Hello from Python! :tada:"
# )

channel_list = sc.api_call(
                      "channels.list",
                      types="private_channel")

pprint([c['is_private'] for c in channel_list['channels']])


# sc.api_call(
#   "channels.info",
#   channel=""
# )
