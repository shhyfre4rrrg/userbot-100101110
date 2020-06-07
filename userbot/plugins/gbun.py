# This is a troll indeed ffs *facepalm*
import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("gbun"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "**Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...**\n"
    no_reason = "**__MOTIVO: Guardi troppi porno.__**"
    await event.edit("**Summoning out le Gungnir ❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1133198248:
            await reply_message.reply("**ATTENZIONE lui è il mio creatore**\n**Come ti permetti di bannarlo!**\n\n**IL TUO ACCOUNT E STATO HACKERATO, paga** [Σάντο](tg://user?id=1133198248) **per riavere il tuo account**😏")
        else:
            jnl=("**Warning!!!**"
                  "[{}](tg://user?id={})"
                  "**𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...**\n\n"
                  "**Name: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim username**: username sconosciuto!\n"
            elif usname != "None":
                jnl += "**Victim username**: @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**MOTIVO: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "**Warning!!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...**\n**MOTIVO: Guardi troppi Porno.**"
        await event.reply(mention)
    await event.delete()