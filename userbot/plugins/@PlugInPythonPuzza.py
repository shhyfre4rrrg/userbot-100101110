# ©@PlugInPython

"""
Commands:
.puzza
"""

import asyncio 
from telethon import events 
from userbot import bot 
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"puzza", outgoing=True)) 
async def _(event): 
    if event.fwd_from: 
        return 
    animation_interval = 0.5
    animation_ttl = range(0, 102) 
    #input_str = event.pattern_match.group(1) 
    #if input_str == "puzza": 
    await event.edit("@Saimo99")
    await event.edit("puzza") 
    animation_chars = [ 
 

"           🏃‍♂💨💨                🚶‍♂",
  

"      🏃‍♂💨💨💨            🚶‍♂       ",


" 🏃‍♂ 💨💨💨💨       🚶‍♂",


"  💨💨💨💨💨   🚶‍♂",


"  💨💨💨💨💨🚶‍♂",


"  💨💨💨🚶‍♂💨",


"  💨💨🤢💨💨",


"  💨🤮💨💨💨",


"  ☠💨💨💨💨",


"**MORTO😵**"

        ] 
 
    for i in animation_ttl: 
            await asyncio.sleep(animation_interval) 
            await event.edit(animation_chars[i % 10])