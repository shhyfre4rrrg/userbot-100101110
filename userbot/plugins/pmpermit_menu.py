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
"""
Support chatbox for pmpermit.
"""
import asyncio
import io 

import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, LESS_SPAMMY, bot
from userbot.system import dev_cmd, command

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
PREV_REPLY_MESSAGE = {}
# ============================================


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         PM = ("Questo è il menù avviabile di"
               f"{DEFAULTUSER}.\n"
               "Indica il motivo perchè sei qui\n"
               "**Scegli tra uno di questi motivi:**\n\n"
               "`1`. Per chattare con me\n"
               "`2`. Per spammare in chat.\n"
               "`3`. Per domandare qualcosa\n")
         ONE = ("La tua richiesta è stata registrata, non spammare in chat avrai una risposta entro 24H. Sono impegnato, a differenza tua probabilmente.\n\n"
                "**⚠️ Verrai bloccato dal bot se continui a spammare ti avviso ⚠️**\n\n"
                "Premi `/start` per tornare al menù principale")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**Ti avevo avvisato,sei stato bloccato dal bot.**")  
         THREE = ("Chiedi pure scrivi tutto in un messaggio non ci sono ti risponderò al più presto.\n**Non spammare se non vuoi essere bloccato dal bot.**")
         LWARN = ("**⚠️ Ultimo avviso ⚠️ non inviare altri messeggi altrimenti verrai bloccato dal bot attendi ti risponderò al più presto.**\nPremi `/start` per tornare al menù principale.")
     
    async with bot.conversation(chat) as conv:
         await bot.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await bot.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await bot.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await bot.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await bot.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await bot.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "3":
             await bot.send_message(chat,THREE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await bot.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await bot.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await bot.send_message(chat, "Comando non valido. Premi `/start` non inviare altri messaggi se non vuoi essere bloccato dal bot.")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await bot.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await bot.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
