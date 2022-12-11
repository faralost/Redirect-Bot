import logging
from telethon import TelegramClient, events
from config import API_ID, API_HASH

logging.basicConfig(level=logging.WARNING, filename='logs.txt')

client = TelegramClient("redirect", API_ID, API_HASH)

from_chats = ('findwork', 'devkz_jobs', 'lost_test')  # replace with your channel usernames
to_chat = "redirect_posts_bot"  # replace with your channel/chat/bot username
tags = ('Python',)  # replace with your tags


@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    if chat.username in from_chats:
        for tag in tags:
            if tag in event.message.message:
                await client.forward_messages(to_chat, event.message)


if __name__ == '__main__':
    client.start()
    print('Bot has started!')
    client.run_until_disconnected()
