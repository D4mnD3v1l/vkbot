# -*- coding: utf-8 -*- 
import random, vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='087308b0c99dbfd7346918020ec35f20f4be30cdf5e3067d465f2aeccd04926cd13915ee59dd5b5291c82')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 203102734)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('87670bdd15d91dd125d6b91f5c5f6f643464d2b19763c3e17d10932b2c93318b630bf7e783544f656cbc1'),
                    server = ('https://cbbot.ifx.su/fe92ou:203102734?code=2806d04f'),
                    ts = ('ljoce616uogctlai584i182okpner743'),
                    random_id = get_random_id(),
                    message='Салам!',
                          chat_id = event.chat_id) 
                
        if 'ауе' in str(event) or 'Ауе' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('87670bdd15d91dd125d6b91f5c5f6f643464d2b19763c3e17d10932b2c93318b630bf7e783544f656cbc1'),
                    server = ('https://cbbot.ifx.su/fe92ou:203102734?code=2806d04f'),
                    ts = ('ljoce616uogctlai584i182okpner743'),
                    random_id = get_random_id(),
                    message='жизнь ворам!',
                          chat_id = event.chat_id)
                
        if 'аниме' in str(event) or 'Аниме' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('87670bdd15d91dd125d6b91f5c5f6f643464d2b19763c3e17d10932b2c93318b630bf7e783544f656cbc1'),
                    server = ('https://cbbot.ifx.su/fe92ou:203102734?code=2806d04f'),
                    ts = ('ljoce616uogctlai584i182okpner743'),
                    random_id = get_random_id(),
                    message='Иди нахуй! ',
                          chat_id = event.chat_id) 
          