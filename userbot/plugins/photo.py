"""Type `.photo` for get **All profile pics of that User**
\n Or type `.photo (number)` to get the **desired number of photo of a User** .
"""

import logging

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot import bot
from userbot.system import dev_cmd

logger = logging.getLogger(__name__)


if 1 == 1:
    name = "Profile Photo"
    client = bot

    @bot.on(dev_cmd(pattern="photo(.*)"))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await bot.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("**ID number you entered is invalid**")
                    return
            except:
                 await event.edit("**Are you Comedy Me ?**")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await bot.send_file(event.chat_id, send_photos)
            else:
                await event.edit("**No photo found of that Nigga , now u Die**")
                return
