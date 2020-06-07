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
"""Reply to a image/sticker .mmf` 'text on top' ; 'text on bottom
"""
import asyncio
import time
from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import DocumentAttributeVideo
from telethon.tl.types import (
DocumentAttributeFilename,
DocumentAttributeSticker,
InputMediaUploadedDocument,
InputPeerNotifySettings,
InputStickerSetID,
InputStickerSetShortName,
MessageMediaPhoto
)

from io import BytesIO
from PIL import Image
from datetime import datetime

import datetime
from collections import defaultdict
import math
import os
import requests
import zipfile

from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.uniborgConfig import Config
from userbot.system import progress, humanbytes, time_formatter, dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@bot.on(dev_cmd("mmf ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un img/sticker/gif `.mms` e il testo, `.mms` testo ; e testo per metterlo pure sotto**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un img/sticker/gif**")
       return
    chat = "@MemeAutobot"
    sender = reply_message.sender
    file_ext_ns_ion = "@memetime.png"
    uploaded_gif = None
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    else:
       await event.edit(f"`{DEFAULTUSER}:`**Inizio la modifica dell'img**")
    file = await bot.download_file(reply_message.media)
    
    async with bot.conversation("@MemeAutobot") as bot_conv:
          try:
            memeVar = event.pattern_match.group(1)
            await silently_send_message(bot_conv, "/start")
            await asyncio.sleep(1)
            await silently_send_message(bot_conv, memeVar)
            await bot.send_file(chat, reply_message.media)
            response = await bot_conv.get_response()
          except YouBlockedUserError: 
              await event.reply("**Please sblocca `@MemeAutobot` **")
              return
          if response.text.startswith("Forward"):
              await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          if "Okay..." in response.text:
            await event.edit("**Inizio la modifica dell'img**")
            thumb = None
            if os.path.exists(thumb_image_path):
                thumb = thumb_image_path
            input_str = event.pattern_match.group(1)
            if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
                os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
            if event.reply_to_msg_id:
                file_name = "meme.png"
                reply_message = await event.get_reply_message()
                to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
                downloaded_file_name = os.path.join(to_download_directory, file_name)
                downloaded_file_name = await bot.download_media(
                    reply_message,
                    downloaded_file_name,
                    )
                if os.path.exists(downloaded_file_name):
                    await bot.send_file(
                        chat,
                        downloaded_file_name,
                        force_document=False,
                        supports_streaming=False,
                        allow_cache=False,
                        thumb=thumb,
                        )
                    os.remove(downloaded_file_name)
                else:
                    await event.edit("File Not Found {}".format(input_str))
            response = await bot_conv.get_response()
            the_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
            files_name = "memes.webp"
            download_file_name = os.path.join(the_download_directory, files_name)
            await bot.download_media(
                response.media,
                download_file_name,
                )
            requires_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "memes.webp"
            await borg.send_file(  # pylint:disable=E0602
                event.chat_id,
                requires_file_name,
                supports_streaming=False,
                caption="Userbot",
                )
            await event.delete()
            sax = await bot.send_message(event.chat_id, "**☠️☠️10 Punti a Griffindor!🔥🔥**")
            await asyncio.sleep(4)
            sax.delete()
          elif not is_message_image(reply_message):
            await event.edit("Invalid message type. Plz choose right message type.")
            return
          else: 
               await bot.send_file(event.chat_id, response.media)

def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False
    
async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response
