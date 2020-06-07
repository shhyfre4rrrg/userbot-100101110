import asyncio
import time
from asyncio import sleep
from os import remove
from datetime import datetime
from telethon import events
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, bot, ALIVE_NAME
from userbot.system import register, errors_handler

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
BOTLOG = True
BOTLOG_CHATID = Var.PRIVATE_GROUP_ID
# ============================================

@register(outgoing=True, pattern=r"^.log(?: |$)([\s\S]*)")
@errors_handler
async def log(log_text):
    """ For .log command, forwards a message or the command argument to the bot logs group """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Chat ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit(f"`{DEFAULTUSER}:`**Inserisci oggetto del log**")
            return
        await log_text.edit(f"`{DEFAULTUSER}:`**log eseguito**")
    else:
        await log_text.edit(f"`{DEFAULTUSER}:`**Serve il log attivo per funzionare!**")
    await sleep(2)
    await log_text.delete()
