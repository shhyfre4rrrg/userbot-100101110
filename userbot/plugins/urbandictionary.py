# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
"""Urban Dictionary
Syntax: .ud Query"""

import asyncurban

from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**Processing...**")
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await event.edit("**Testo: {}**\n\n**Definizione: {}**\n\n**Esempio: {}**".format(mean.word, mean.definition, mean.example))
    except asyncurban.WordNotFoundError:
        await event.edit("**Nessun risultato trovato per " + word + "**")
