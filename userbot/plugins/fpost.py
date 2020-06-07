# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Command:
.fpost word"""

import string

from telethon import events
from telethon.tl import types
from userbot import bot
from userbot.system import dev_cmd

msg_cache = {}


@bot.on(dev_cmd(pattern=f"fpost", outgoing=True))
async def _(event):
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()

    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in bot.iter_messages(None, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        await bot.forward_messages(destination, msg_cache[c])
