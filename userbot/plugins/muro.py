import asyncio
from telethon import events
from platform import uname 
from userbot import bot
from userbot.system import dev_cmd

'''Command and ideas by Mattew (github.com/CometaLunare)'''

@bot.on(dev_cmd(pattern=f"muro", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.3
    animation_ttl = range(0, 18)
    await event.edit("muro")
    animation_chars = [
        
            "||            🚙",
            "||         🚙",
            "**Una piotta e dieci così, terza marcia, terza marcia, terza marcia.**",
            "__NON CI SONO PROBLEMI, NON CI SONO PROBLEMI__",
            "__Vi insegno a guidare...__",
            "||     🚙",
            "||  🚙",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🟢",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🟠",
            "🚦 **QUANDO IL SEMAFORO È ROSSO** 🔴",
            "Si fa così, si fa così: taac.",
            "Je imbocchi qua, je rigiri qua, fratellì, così.",
            "|| 🚙",
            "||🚙",
            "Bada fratellì, **ho sfondato tutto fratellì**, ho sfonnato tutto.",
            "__Ho preso er muro fratellì, te dico fermati fratellì. Ho preso er muro. __♿️"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])