
"""BarCode Generator
Command .barcode"""

import asyncio
import barcode
import os
import time

from barcode.writer import ImageWriter
from datetime import datetime
from userbot import ALIVE_NAME, bot
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@bot.on(dev_cmd(pattern="barcode (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"`{DEFAULTUSER}:`**Creo Stickers...**")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: .barcode <testo>"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: .barcode <testo>"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await bot.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await event.edit(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("**Creato BarCode in {} sec**".format(ms))
    await asyncio.sleep(5)
    await event.delete()
