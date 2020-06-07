import asyncio
import time

from asyncio import wait, sleep
from telethon import events
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.system import register



@register(outgoing=True, pattern="^.spam (.*)")
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID,
            "#SPAM\n"
            "Spam eseguita"
            )


@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM\n"
                "Bigspam eseguita"
                )


@register(outgoing=True, pattern="^.cspam (.*)")
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID,
            "#CSPAM\n"
            "TSpam eseguita")


@register(outgoing=True, pattern="^.delayspam (.*)")
async def delayspam(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID,
            "#DelaySPAM\n"
            "DelaySpam eseguita"
            )


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "**PicSpam eseguita**")


@register(outgoing=True, pattern="^.repeat")
async def repeat(e):
    message = e.text[10:]
    count = int(e.text[8:10])
    repmessage = message * count
    await e.respond(repmessage)
    await e.delete()
    

@register(outgoing=True, pattern="^.repeats")
async def repeats(e):
    message = e.text[10:]
    count = int(e.text[8:10])
    repmessage = message * count
    await wait([e.respond(repmessage)for i in range(count)])
    await e.delete()


@register(outgoing=True, pattern="^.wspam (.*)")
async def wspam(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID,
            "#WSPAM\n"
            "WSpam eseguita")
