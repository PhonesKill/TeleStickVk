from termcolor import colored
import vk
import emoji
import requests
import json
import re
def follower(api,response,text,lenUpdates):
	for a in range(lenUpdates):
		if response['updates'][a]['type'] == 'group_join':
			response = response['updates'][a]['object']
			follower = response['user_id']
			api.messages.send(user_id=follower,message=text)
def messages(api,response,text,lenUpdates):
	for a in range(lenUpdates):
		if response['updates'][a]['type'] == 'message_new':
			response = response['updates'][a]['object']
			message = response['text']
			message = message.split(' ')
			if len(message) == 2 and (message[0])[0] == ':':
				message[0] = message[0].replace(':','')
				try:
					file = open('/home/linux/VkBot/'+message[0]+'.txt')
					smail = emoji.demojize(message[1]) + '\n'
					lines = file.readlines()
					lenLines = len(lines)
					for line in range(lenLines):
						if lines[line] == smail:
							api.messages.send(peer_id=response['peer_id'],attachment=lines[line-1])
					file.close()
				except FileNotFoundError:
					api.messages.send(peer_id=response['peer_id'],message=text)
			elif len(message) != 2 and (message[0])[0] == ':':
				api.messages.send(peer_id=response['peer_id'],message=text)		
token = 'your_token'
session = vk.Session(access_token=token)
api = vk.API(session,v='5.80')
longPoll = api.groups.getLongPollServer(group_id=168336094)
server, key, ts = longPoll['server'], longPoll['key'], longPoll['ts']
text = 'Неверная команда, попробуйте снова!'
join = 'Спасибо за вступление в группу нашего Бота!'
while True:
	response = requests.get('{server}?act=a_check&key={key}&ts={ts}&wait=20&mode=2&version=2'
		.format(server=server, key=key, ts=ts)).json()
	if response['updates'] and len(response['updates']) != 0:
		lenUpdates = len(response['updates'])
		messages(api,response,text,lenUpdates)
		follower(api,response,join,lenUpdates)
	ts = response['ts']
