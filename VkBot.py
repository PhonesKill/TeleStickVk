from termcolor import colored
import vk
import requests
import json
import re

def messages(api,response,text,lenUpdates):
	for a in range(lenUpdates):
		if response['updates'][a]['type'] == 'message_new':
				api.messages.send(user_id=response['updates'][a]['object']['peer_id'],
								 message=text)

token = '7afc6701df497d8fae992b8f460a35c2eba2b243dbcca36d3643740a8080e800b3d373f4abf926388c5e7'
session = vk.Session(access_token=token)
api = vk.API(session,v=5.8)
longPoll = api.groups.getLongPollServer(group_id=168336094)
server, key, ts = longPoll['server'], longPoll['key'], longPoll['ts']
text = 'Вот список моих команд:\n1) Шутка.\n2) Оскорбление.'

while True:
	response = requests.get('{server}?act=a_check&key={key}&ts={ts}&wait=20&mode=2&version=2'
		.format(server=server, key=key, ts=ts)).json()
	if response['updates'] and len(response['updates']) != 0:
		lenUpdates = len(response['updates'])
		messages(api,response,text,lenUpdates)
		print(response)
	ts = response['ts']