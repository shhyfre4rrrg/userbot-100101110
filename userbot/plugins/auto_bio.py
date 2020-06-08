"""Auto Profile Updation Commands
.autopp"""
import asyncio
import time
from telethon import functions
from telethon.errors.rpcerrorlist import FloodWaitError
from userbot import bot 
from userbot.system import dev_cmd


DEL_TIME_OUT = 70


@bot.on(dev_cmd("autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f" 🌐 {HM} DEL {DMY} "
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await bot.send_message(  # pylint :disable=E0602
            # Var.PRIVATE_GROUP_ID,  # pylint:disable=E0602
            #     "Changed Profile Picture"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

