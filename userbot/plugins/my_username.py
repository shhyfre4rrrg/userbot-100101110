import asyncio

from telethon import events, functions, types
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"taglist", outgoing=True))
async def taglist(event):
    """ For .taglist command, get a list of your reserved usernames. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)
