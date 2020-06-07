import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import ALIVE_NAME, bot
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd("scan ?(.*)"))
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
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Analizzo il file...**")
    async with bot.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("**Please sblocca `@DrWebBot` **")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"`{DEFAULTUSER}:`Please vai su @DrWebBot e select la lingua.") 
          	else: 
          			await event.edit(f"`{DEFAULTUSER}:`Scan antivirus completata. Ecco i resultati.**\n {response.message.message}")
