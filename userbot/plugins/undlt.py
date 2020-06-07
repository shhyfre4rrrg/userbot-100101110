import asyncio

from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern="undlt"))
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await bot.get_admin_log(event.chat_id,limit=5, search="", edit=False, delete=True)
        for i in a:
          await event.reply(i.original.action.message)
    else:
        await event.edit("**Non hai i permessi per usare questo comando**")
        await asyncio.sleep(3)
        await event.delete()
