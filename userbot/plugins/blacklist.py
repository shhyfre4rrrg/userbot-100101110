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
"""Filters
Available Commands:
.addblacklist
.listblacklist
.rmblacklist"""

import asyncio
import re
import io
import userbot.plugins.sql_helper.blacklist_sql as blacklist_sql
from telethon import events, utils
from telethon.tl import types, functions
from userbot.system import dev_cmd
from userbot import CMD_HELP, bot

 
@bot.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = blacklist_sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                await event.reply("**Non ho i permessi sufficenti in questa chat**")
                blacklist_sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@bot.on(dev_cmd("addblacklist ((.|\n)*)"))
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        blacklist_sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.edit("**Aggiunto {} alla blacklist di questa chat**".format(len(to_blacklist)))


@bot.on(dev_cmd("listblacklist"))
async def on_view_blacklist(event):
    all_blacklisted = blacklist_sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "**BlackList in questa Chat:**\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👉 {trigger} \n"
    else:
        OUT_STR = "**Nessuna BlackList. Salva usando** `.addblacklist`"
    if len(OUT_STR) > 4095:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="**BlackList in questa Chat**",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@bot.on(dev_cmd("rmblacklist ((.|\n)*)"))
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if blacklist_sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"**Rimosso {successful} / {len(to_unblacklist)} dalla blacklist**")
