"""Send Chat Actions
Syntax: .scha <option> <time in sec>
scha options:
typing
contact
game
location
voice
round
video
photo
document
cancel"""

import asyncio
from userbot import bot
from userbot.system import dev_cmd
 
 
@bot.on(dev_cmd("scha ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with bot.action(event.chat_id, action):
        await asyncio.sleep(86400)  # type for 10 seconds
