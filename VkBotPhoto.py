from termcolor import colored
import vk_api
import emoji
import requests
import json
import re
session = vk_api.VkApi('login','password')
session.auth()
vk = session.get_api()
photos = vk.photos.getAll(owner_id='id группы')
photos = json.dumps(photos)
photos = json.loads(photos)
photoId = ''
for i in range(len(photos['items'])):
	photoId += '\n' + 'photo' + str(photos['items'][i]['owner_id']) + '_' + str(photos['items'][i]['id']) + '\n'+ str(emoji.demojize(photos['items'][i]['text']))
file = open('путь к файлу .txt','w')
file.write(photoId)
file.close()
	