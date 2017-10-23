import os
from flask import Flask, request
from slackclient import SlackClient
from pprint import pprint
import json
import requests
import re

#################################
### EXPORTING DATA FROM SLACK ###
#################################

with open('./api_token_export.json') as data_file:
    credentials = json.load(data_file)

token_export = credentials['token']

sc_export = SlackClient(token_export)

channel_list = sc_export.api_call(
                      "conversations.list",
                      types="private_channel",
                      exclude_archived=1
                      )

channels = { c['id']:c['name'] for c in channel_list['channels']}

messages = {}

for (k,v) in channels.items():
  messages[v] = sorted(sc_export.api_call(
                            "conversations.history",
                             channel=k,
                             limit = 1000
                            )['messages'], key= lambda d: d['ts'])

# test = []
# for m in messages[channel_list['channels'][0]['name']]:
#   if ('file' in m):
#     if('preview' in m['file']):
#       test.append(m['file']['preview'])
#   else:
#     test.append(m['text'])

#print("****************test")
#print("****************" + channel_list['channels'][0]['name'])
#pprint(test)
#pprint(messages['bash-legacy'])

import json
with open('code_snippets.json', 'w') as outfile:
    json.dump(messages, outfile)

#################################
### IMPORTING DATA FROM SLACK ###
#################################

with open('./api_token_import.json') as data_file:
    credentials = json.load(data_file)

token_import = credentials['token']

sc_import = SlackClient(token_import)

# def text(m):
#   pre = re.compile('<pre>(.*)</pre>')
#   if ('file' in m):
#     if('preview_highlight' in m['file']):
#       return '\n'.join(pre.findall(m['file']['preview_highlight']))
#print(preview(messages['bash-legacy'][1]))

def if_file(m):
  if 'file' in m:
    return m['file']

# for m in messages['bash-legacy']:
#   if 'file' in m:
#     sc_import.api_call(
#       "chat.unfurl",
#       channel="#bash",
#       unfurls=m['file']['permalink_public']
#       )
#   else:
#     sc_import.api_call(
#       "chat.postMessage",
#       channel="#bash",
#       text=m['text']
#     )

for c in channels.values() :
  print(c)
  for m in messages[c]:
      sc_import.api_call(
        "chat.postMessage",
        channel="#{0}".format(c),
        text=m['text'],
        attachments=if_file(m)
      )




with open('./code_snippets.json') as data_file:
    messages_json = json.load(data_file)

pprint(messages_json)
