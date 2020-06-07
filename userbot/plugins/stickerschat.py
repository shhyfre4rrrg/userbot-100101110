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

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.system import dev_cmd
from userbot import CMD_HELP, ALIVE_NAME, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@bot.on(dev_cmd(pattern="ext2 ?(.*)"))
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
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Creo Stickers...**")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Please sblocca** `@QuotLyBot`")
              return
          if response.text.startswith("Hi!"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
