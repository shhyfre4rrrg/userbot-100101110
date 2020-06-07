from telethon import events
import os
import requests
import json
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("ddg (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit("**Vedi su 🦆 DuckDuckGo i risultati:\n🔎 [{}]({})**".format(input_str, link))
    else:
        await event.edit("**Qualcosa è andato storto, riprova più tardi**")
