#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Vai su my.telegram.org
Fai il login nel tuo account Telegram
Click API Development Tools
Crea una nuova applicazione e inserisci i requisiti necessari""")
APP_ID = int(input("Inserisci APP ID qui: "))
API_HASH = input("Inserisci API HASH qui: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
