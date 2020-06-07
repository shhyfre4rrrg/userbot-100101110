"""Commands:
.fadmin"""

import asyncio

from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"fadmin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    #input_str = event.pattern_match.group(1)
    #if input_str == "fadmin":
    await event.edit("fadmin")
    animation_chars = [
        
            "**Promozione User ad Admin...**",
            "**Attivazione di tutti i Permessi...**",
            "**(1) Inviare Messaggi: ☑️**",
            "**(1) Inviare Messaggi: ✅**",
            "**(2) Inviare Media: ☑️**",
            "**(2) Inviare Media: ✅**",
            "**(3) Inviare stickers & GIF: ☑️**",
            "**(3) Inviare stickers & GIF: ✅**",    
            "**(4) Inviare sondaggi: ☑️**",
            "**(4) Inviare sondaggi: ✅**",
            "**(5) Inviare link con anteprima: ☑️**",
            "**(5) Inviare link con anteprima: ✅**",
            "**(6) Aggiungere utenti: ☑️**",
            "**(6) Aggiungere utenti: ✅**",
            "**(7) Fissare messaggi: ☑️**",
            "**(7) Fissare messaggi: ✅**",
            "**(8) Cambiare le info chat: ☑️**",
            "**(8) Cambiare le info chat: ✅**",
            "**Permessi attivati con successo**",
            "**Promosso con Successo da: @IOIIIOIIIOI**"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 20])
