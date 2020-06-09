import asyncio
import requests , re , random
import urllib , os
from time import sleep
from telethon.tl import functions
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot import bot
from userbot.system import dev_cmd


COLLECTION_STRING = [

  "avengers-logo-wallpaper",

  "avengers-hd-wallpapers-1080p",

  "iron-man-wallpaper-1920x1080",

  "iron-man-wallpapers",

  "Marvel-Shield-iPhone-Wallpaper",

  "Shield-Logo-Wallpaper",

  "Marvel-Shield-Logo-Wallpaper",

  "Agents-of-Shield-Wallpaper",

  "Thor-Wallpaper-1920x1080",

  "Thor-Wallpapers",

  "Avengers-HD-Wallpapers-1080p",

  "Avengers-Age-of-Ultron-Wallpaper",

  "Avengers-Civil-War-Wallpaper",

  "Avengers-2-Wallpapers",

  "Avengers-Logo-Wallpaper",

  "Marvel-Avengers-Desktop-Wallpaper",

  "3D-Deadpool-Logo-Wallpaper",

  "Cool-Deadpool-Wallpaper",

  "Thor-Wallpaper-HD"
  
]

async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1) 
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")


@bot.on(dev_cmd(pattern="marveldp ?(.*)"))
async def main(event):
    await event.edit("**Avvio Marvel Profile Pic...**")
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600) #Edit this to your required needs
