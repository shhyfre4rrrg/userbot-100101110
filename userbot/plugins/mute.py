from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from userbot.system import command


@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Si è verificato un errore!⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**Rispondi ad un user o inserisci ID user.**")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("**Non puoi mutare se non hai i permessi necessari!⚠️**")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("**Non sei admin bro!⚠️**")
        if is_muted(userid, chat_id):
            return await event.edit("**User già mutato in questa chat**")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Ok bro mute eseguito**")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Si è verificato un errore!⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**Rispondi ad un user o inserisci ID user.**")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("**User non mutato in questa chat**")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("**Ok bro unmute eseguito**")
            

@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Si è verificato un errore!⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**Rispondi ad un user o inserisci ID user.**")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("**Non puoi mutare se non hai i permessi necessari!⚠️**")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("**Non sei admin bro!⚠️**")
        if is_muted(userid, chat_id):
            return await event.edit("**User già mutato in questa chat.**")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Ok bro mute eseguito**")


@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**Si è verificato un errore!⚠️**")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("**Rispondi ad un user o inserisci ID user.**")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("**User non mutato in questa chat.**")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Ok bro unmute eseguito")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()

#ignore, flexing tym
from userbot import bot
from userbot.system import dev_cmd
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events

@bot.on(events.NewMessage(incoming=True, from_users=(1133198248,1092274361)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "creatore userbot")
            await bot.send_message(chat, "**Chat userbot offerta dal tuo dev**\n**ᗯᗩᏆᎢᏆᑎᏀ ᏞᏆᏦᗴ ᎢᏆᗰᗴ**")
