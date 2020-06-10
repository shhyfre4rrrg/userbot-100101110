# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @bot.on(100101110
#
"""Commands:
.clock
.moon
.lmoon
.smoon
.tmoon
.ok
.wtf"""

import asyncio

from collections import deque
from telethon import events
from userbot import CMD_HELP, bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"clock", outgoing=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)

@bot.on(dev_cmd(pattern=f"moon", outgoing=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)

@bot.on(dev_cmd(pattern=r"lmoon"))
async def _(event):
    if event.fwd_from:
        return 
    await event.edit("🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕")

@bot.on(dev_cmd(pattern=f"smoon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "smoon":
    await event.edit("smoon")
    animation_chars = [

            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",    
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])

@bot.on(dev_cmd(pattern=f"tmoon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 117)
    #input_str = event.pattern_match.group(1)
    #if input_str == "tmoon":
    await event.edit("tmoon")
    animation_chars = [

            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 117])

@bot.on(dev_cmd("oh ?(.*)", outgoing=True))
async def lol(e):
    await e.edit(
"\n██╗░░░░░░█████╗░██╗░░░░░"
"\n██║░░░░░██╔══██╗██║░░░░░"
"\n██║░░░░░██║░░██║██║░░░░░"
"\n██║░░░░░██║░░██║██║░░░░░"
"\n███████╗╚█████╔╝███████╗"
"\n╚══════╝░╚════╝░╚══════╝") 
 
@bot.on(dev_cmd(pattern=f"ok", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.0001
    animation_ttl = range(0, 90)
    #input_str = event.pattern_match.group(1)
    #if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
            "F",
            "U",
            "C",
            "K",
            "Y",
            "O",
            "U",
            "F",
            "C",
            "FK",
            "CU",
            "FUCK",
            "UCK",
            "C",
            "K",
            "U",
            "F",
            "OK CHAMP 😇"
        ]

    for i in animation_ttl:        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])

@bot.on(dev_cmd(pattern=f"wtf", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    #input_str = event.pattern_match.group(1)
    #if input_str == "wtf":
    await event.edit("wtf")
    animation_chars = [
            "What",
            "What The",
            "What The Fuck",
            "[What The Fuck Bro](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)"
        ]

    for i in animation_ttl:        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5 ])
