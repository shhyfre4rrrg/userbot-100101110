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
"""Commands:
.avast
.avast1
.call
.hack
.linux
.macos
.stock
.windows"""

import asyncio
from telethon import events
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd(pattern=f"avast", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "avast":
    await event.edit("avast")
    animation_chars = [
        
            "**Downloading File..**",
            "**File Downloaded....**",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nRicerca: 01 of 01 Files Scansione...\n\nSTATUS: Nessun Virus Rilevato...**"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@bot.on(dev_cmd(pattern=f"avast1", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "avast1":
    await event.edit("avast1")
    animation_chars = [
        
            "**Downloading File..**",
            "**File Downloaded....**",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ **",
            "**Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nRicerca: 01 of 01 Scansione...\n\nSTATUS:⚠️Virus Rilevato⚠️\nINFO: Torzan, Spyware, Adware**"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@bot.on(dev_cmd(pattern=f"call", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    #input_str = event.pattern_match.group(1)
    #if input_str == "call":
    await event.edit("call")
    animation_chars = [
        
            "**Chiamata alla sede di Telegram...**",
            "**Chiamata Connessa**",
            "**Telegram: Salve, risponde la sede di Telegram. Chi è lei?**",
            f"{DEFAULTUSER}:**Salve sono** {DEFAULTUSER} ,**Devo parlare con il mio socio ,Pavel Durov**",
            "**User Autorizzato**",
            "**Chiamata a Pavel Durov** **+6969696969**",
            "**Chiamata Connessa**",  
            f"{DEFAULTUSER}:**Banna questo account da Telegram**",
            "**Pavel: Posso sapere chi sei?**",
            f"{DEFAULTUSER}:**Yo bro, sono il tuo socio**",
            "**Pavel: OMG!!! Ma è da tanto che non ci vediamo, bro...\nMi assicurerò io che l'account venga bloccato entro 24 ore.**",
            f"{DEFAULTUSER}:**Grazie, a dopo bro.**",
            "**Pavel: Ma va bro, telegram è nostro. Chiamami quando sei libero**",
            f"{DEFAULTUSER}:**C'è qualche problema bro?🤔**",
            "**Pavel: Sì bro, c'è un bug in telegram v8.6.9.\nNon sono in grado di risolverlo. Mi, aiuti a correggere il bug?**",
            f"{DEFAULTUSER}:**Inviami tutto in chat, risolverò il bug.**",
            "**Pavel: Grazie bro \nCi sentiamo :)**",
            "**Chiamata Disconnessa.**"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])


@bot.on(dev_cmd(pattern=f"hack", outgoing=True))
async def _(event):   
    if event.fwd_from:       
        return   
    animation_interval = 2   
    animation_ttl = range(0, 12)    
    #input_str = event.pattern_match.group(1)   
    #if input_str == "hack":       
    await event.edit("hack")       
    animation_chars = [
        
            "**Connessione a Telegram Data Center**",
            f"Target Selected By Hacker: {DEFAULTUSER}",
            "**Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
            "**Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
            "**Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",    
            "**Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
            "**Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
            "**Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
            "**Hacking... 84%\n█████████████████████▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**",
            "**Hacking... 100%\n█████████HACKED███████████ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
            f"**Account Hackerato...\n\nPaga 100€ a** {DEFAULTUSER} **Per Rimuovere questo VIRUS**\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Server Database di Telegram Hackerato**\n\n\n🔹**Output:** Successful"
        ]

    for i in animation_ttl:          
            await asyncio.sleep(animation_interval)           
            await event.edit(animation_chars[i % 12])


@bot.on(dev_cmd(pattern=f"linux", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "linux":
    await event.edit("linux")
    animation_chars = [
        
            "**Connessione a Linux...**",
            "**Inizializza Linux Login.**",
            "**Loading Linux... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Linux... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Linux... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Loading Linux... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Linux... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Linux... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Linux... 89%\n█████████████████████▒▒▒▒ **",
            "**Loading Linux... 100%\n█████████████████████████ **",
            "**Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Linux**\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@bot.on(dev_cmd(pattern=f"macos", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "macos":
    await event.edit("macos")
    animation_chars = [
        
            "**Connessione a Hackintosh...**",
            "**Inizializza Hackintosh Login.**",
            "**Loading Hackintosh... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Hackintosh... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Hackintosh... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Loading Hackintosh... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Hackintosh... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Hackintosh... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Hackintosh... 89%\n█████████████████████▒▒▒▒ **",
            "**Loading Hackintosh... 100%\n█████████████████████████ **",
            "**Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Hackintosh**\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@bot.on(dev_cmd(pattern=f"stock", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "stock":
    await event.edit("stock")
    animation_chars = [
        
            "**Connessione a Symbian OS...**",
            "**Inizializza Symbian OS Login.**",
            "**Loading Symbian OS... 0%\n█████████████████████████ **",
            "**Loading Symbian OS... 3%\n█████████████████████▒▒▒▒ **",
            "**Loading Symbian OS... 9%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Loading Symbian OS... 23%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Symbian OS... 39%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Symbian OS... 69%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Symbian OS... 89%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Symbian OS... 100%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Symbian OS**\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])


@bot.on(dev_cmd(pattern=f"windows", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "windows":
    await event.edit("windows")
    animation_chars = [
        
            "**Connessione a Windows 10...**",
            "**Inizializza Windows 10 Login.**",
            "**Loading Windows 10... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Windows 10... 3%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Windows 10... 9%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",    
            "**Loading Windows 10... 23%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Windows 10... 39%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Windows 10... 69%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **",
            "**Loading Windows 10... 89%\n█████████████████████▒▒▒▒ **",
            "**Loading Windows 10... 100%\n█████████████████████████ **",
            "**Welcome...\n\nStock OS: Symbian OS\nCurrent OS: Windows 10**\n\n**My PC Specs:**\n\n **CPU:** __2.9GHz Intel Core i9-8950HK (hexa-core, 12MB cache, up to 4.8GHz)__\n\n**Graphics:** __Nvidia GeForce GTX 1080 OC (8GB GDDR5X)__\n\n**RAM:** __32GB DDR4 (2,666MHz)__\n\n**Screen:** __17.3-inch, QHD (2,560 x 1,440) 120Hz G-Sync__\n\n**Storage:** __512GB PCIe SSD, 1TB HDD (7,200 rpm)__\n\n**Ports:** __2 x USB 3.0, 1 x USB-C 3.0, 1 x USB-C (Thunderbolt 3), HDMI, mini DisplayPort, Ethernet, headphone jack, microphone jack__\n\n**Connectivity:** __Killer 1550 802.11ac Wi-Fi, Bluetooth 5.0__\n\n**Camera:** __Alienware FHD camera, Tobii IR Eye-tracking with Windows Hello__\n\n**Size:** __16.7 x 13.1 x 1.18 inches (42.4 x 33.2 x 2.99cm; W x D x H)__"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
