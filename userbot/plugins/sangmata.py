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

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd(pattern=("sg ?(.*)")))
async def _(event):
   if event.fwd_from:
      return 
   if not event.reply_to_msg_id:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
      return
   reply_message = await event.get_reply_message() 
   if not reply_message.text:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
      return
   chat = "@SangMataInfo_bot"
   sender = reply_message.sender
   if reply_message.sender.bot:
      await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
      return
   await event.edit(f"`{DEFAULTUSER}:`**Ricerca Storico...**")
   async with bot.conversation(chat) as conv:
         try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
            await bot.forward_messages(chat, reply_message)
            response = await response 
         except YouBlockedUserError: 
            await event.reply("**Please sblocca** `@Sangmatainfo_bot`")
            return
         if response.text.startswith("Forward"):
            await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
         else: 
            await event.edit(f"{response.message.message}")


@bot.on(dev_cmd(pattern=("gid ?(.*)")))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user.**")
       return
    chat = "@getidsbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Ricerca Info...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Please sblocca** `@getidsbot`")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else: 
             await event.edit(f"{response.message.message}")
