import twitch
import requests
import queue
from config import CONFIG

class TwitchBot():
    def __init__(self, message_queue):
        global CONFIG 

        username          = CONFIG['username']
        client_id         = CONFIG['client-id']
        twitch_chat_oauth = CONFIG['twitch-chat-oauth']
        channel           = CONFIG['channel']

        self.message_queue = message_queue

        self.chat = twitch.Chat(channel='#' + channel,
                                nickname=username,
                                oauth=twitch_chat_oauth,
                                helix=twitch.Helix(client_id=client_id, use_cache=True))
        self.chat.subscribe(self.handle_message)

        print("Twitch Bot has initialized")

    def handle_message(self, message):
        text = message.sender + ": " + message.text
        self.message_queue.put(text)

        print(text)
   