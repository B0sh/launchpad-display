import sys
import irc.bot
import requests
import queue
from config import CONFIG

# https://github.com/twitchdev/chat-samples/blob/master/python/chatbot.py
# Possibly later I can go back and add in commands

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel, message_queue):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        self.message_queue = message_queue

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/helix/users?login=' + channel
        headers = {'Client-ID': client_id }
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['data'][0]['id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print ('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
    
    def parse_tags(self, tags):
        result = {}
        for tag in tags:
            result[tag['key']] = tag['value']
        return result

    def on_welcome(self, c, e):
        print ('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)


    def on_pubmsg(self, c, e):
        # print (e)
        tags = self.parse_tags(e.tags)
        message = tags['display-name'] + ": " + e.arguments[0]
        self.message_queue.put(message)
        return
        
def main(twitch_message_queue):
    global CONFIG 
    username  = CONFIG['username']
    client_id = CONFIG['client-id']
    token     = CONFIG['token']
    channel   = CONFIG['channel']

    bot = TwitchBot(username, client_id, token, channel, twitch_message_queue)
    bot.start()

    return bot

if __name__ == "__main__":
    main()