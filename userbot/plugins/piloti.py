import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.10

    animation_ttl = range(0, 102)

    input_str = event.pattern_match.group(1)

    if input_str == "pilota":

        await event.edit(input_str)

        animation_chars = [
 
"🛫",
"**PILOTA1727**:__Siamo partiti__",
"**CENTRALE**:__Speriamo che il viaggio vada bene__",
"**PILOTA1727**:__Andrà tutto bene__",
                  "**1 ora dopo**",
"✈️✈️✈️✈️☄",                     
"💥💥💥",
"**CENTRALE**:__Cosa succede lì dentro?__",
"**PILOTA 1727**:__Ho sfonnato tutto fratellì__",
]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])