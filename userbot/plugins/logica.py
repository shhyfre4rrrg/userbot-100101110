# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#
"""Commands:
.logic"""

import asyncio
import random

from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"logic", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**Attendi 2sec sto pensando 🤔...**")
    await asyncio.sleep(2)
    x=(random.randrange(1,7))
    if x==1:
        await event.edit("**La logica è una cosa e il buon senso un’altra.**")
    if x==2:
        await event.edit("**Ama la vita più della sua logica.**")
    if x==3:
        await event.edit("**La logica vi porterà da A a B. L’immaginazione vi porterà dappertutto.**")
    if x==4:
        await event.edit("**Le relazioni tra uomini e donne non si possono spiegare mediante la logica.**")
    if x==5:
        await event.edit("**Nella realtà non avviene nulla che corrisponda rigorosamente alla logica.**")
    if x==6:
        await event.edit("**Una mente tutta logica è come un coltello tutto lama. Fa sanguinare la mano che lo usa.**")
    if x==7:
        await event.edit("**Ciò che sfugge alla logica è quanto v’è di più prezioso in noi stessi.**")
