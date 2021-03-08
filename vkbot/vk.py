# -*- coding: utf-8 -*- 
import random, vk_api, vk
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='14a1f98a8ffb280447fbc5f0a95581c00a79351b0e69c7a8934cfa624017ca73010c3195e40cf1fcc5dc5')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 203102734)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if "228" in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='1337', chat_id = event.chat_id) 
        """a = 1
        while a < 100:
            a = a+1
            vk.messages.send(random_id = get_random_id(), message='ауе!', chat_id = event.chat_id)"""
            
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Салам' in str(event) or 'Здарова' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Здарова!', chat_id = event.chat_id) 
                
        if 'ауе' in str(event) or 'Ауе' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='жизнь ворам!', chat_id = event.chat_id)
                
        if 'аниме' in str(event) or 'Аниме' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Аниме - говно', chat_id = event.chat_id)
        """else:
            vk.messages.send(random_id = get_random_id(), message='Не понял', chat_id = event.chat_id)"""
