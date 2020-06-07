# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
  
from telethon import events
import subprocess
import asyncio
import time
from userbot.system import command

@command(pattern="^.cmd", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**ℹ️ LISTA PLUG-IN 🔍**\n\n{o}\n\n**ℹ️ SUGGERIMENTO:**\nSe hai problemi con i plugin\nVisita ~ @IOIIIOIIIOI ~"
    await event.edit(OUTPUT)
