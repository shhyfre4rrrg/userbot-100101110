# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#

import asyncio
import io
import math
import urllib.request
import datetime
import os
import random
import textwrap

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker
from telethon.tl.types import InputMessagesFilterDocument
from telethon import events

from os import remove
from PIL import Image, ImageDraw, ImageFont

from userbot import bot, CMD_HELP, ALIVE_NAME
from userbot.system import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@register(outgoing=True, pattern="^.ext1(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return  
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad una foto**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad una foto**")
       return
    chat = "@BuildStickerBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Creo Stickers...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=164977173))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Please sblocca** `@BuildStickerBot`")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"`{DEFAULTUSER}:`Please vai su @DrWebBot e select la lingua.") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)
