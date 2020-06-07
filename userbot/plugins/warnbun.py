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

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("warn1"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`WARN  1/3 avvertimento...\nATTENTO!...\nMOTIVO: Guardi i Porno`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(dev_cmd("warn2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`WARN  2/3  avvertimento...\nATTENTO!...\nMOTIVO: rubi caramelle ai bambini`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(dev_cmd("warn3"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`WARN  3/3...\nBAN!!!...\nMOTIVO BAN: hai rotto il cazzo`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(dev_cmd("warn0"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`WARN RESETTATI...\nHai  0/3  warn`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(dev_cmd("ocb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**ATTENZIONE..\n\nBatteria Sotto Il 10%, Per Favore Ricarica**"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@bot.on(dev_cmd("fw"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`FLOODWAIT ERROR:\nMotivo:telethon.errors.rpcerrorlist.FloodWaitError: Attendi 546578265716823 secondi (causato da troppi messaggi)`"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
