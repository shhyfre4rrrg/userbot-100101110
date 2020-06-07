import asyncio
import datetime
import os
import random
import textwrap
import io
import math

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker

import urllib.request
from os import remove
from PIL import Image, ImageDraw, ImageFont

from userbot import bot, CMD_HELP, ALIVE_NAME
from userbot.system import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@register(outgoing=True, pattern="^.frybot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a foto/sticker**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a foto/sticker**")
       return
    chat = "@image_deepfrybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Creo img/sticker...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Please sblocca `@image_deepfrybot` **")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else: 
                await bot.send_file(event.chat_id, response.message.media)
