# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
"""Commands:
.bye"""

import time

from telethon.tl.functions.channels import LeaveChannelRequest
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("bye", outgoing=True))
async def bye(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit('**Esco dalla chat!**')
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('**Non puoi abbandonare la chat**')
