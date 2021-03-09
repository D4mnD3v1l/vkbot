# -*- coding: utf-8 -*- 
import random, vk_api, vk
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='14a1f98a8ffb280447fbc5f0a95581c00a79351b0e69c7a8934cfa624017ca73010c3195e40cf1fcc5dc5')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 203102734)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
       
        """class VkBot:
        
            def __init__(self, user_id):
                self._USER_ID = user_id
                self._USERNAME = self._get_user_name_from_vk_id(user_id)"""
                
        """def _get_user_name_from_vk_id(self, user_id):
                request = requests.get("https://vk.com/id"+str(user_id))
                bs = bs4.BeautifulSoup(request.text, "html.parser")
                user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
                
                return user_name.split()[0]"""         
                       
        """a = 1
        while a < 100:
            a = a+1
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='̛̾͌͆̎̎̈̎͛͗͐̄̽̊̃̿͋͌͒̔͛̍̋̀̾̀̀̏̉͒̋́͑́͌͊̇̏̌̃̂̓̀͂̇̾͑̇̍̿̈́̕̚̚̕̕̕͝͠͠͝͝͝, chat_id = event.chat_id)"""
        """else:
            vk.messages.send(random_id = get_random_id(), message='Не понял', chat_id = event.chat_id)"""
        
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Салам' in str(event) or 'Здарова' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Здарова!', chat_id = event.chat_id) 
                
        elif 'ауе' in str(event) or 'Ауе' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='жизнь ворам!', chat_id = event.chat_id)
                
        elif 'аниме' in str(event) or 'Аниме' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Аниме - говно', chat_id = event.chat_id)
        
        elif 'Да' in str(event) or 'да' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Пизда!', chat_id = event.chat_id)
        
        elif 'Нет' in str(event) or 'нет' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Пидора ответ!', chat_id = event.chat_id)
                
        elif '300' in str(event) or 'триста' in str(event) or 'Триста' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='Отсоси у тракториста!', chat_id = event.chat_id)
                
        elif 'Тракторист сегодня я отсоси ты у меня' in str(event):
            if event.from_chat:
                vk.messages.send(random_id = get_random_id(), message='В трактористы ты не годен, отсоси и будь свободен!', chat_id = event.chat_id)
        
