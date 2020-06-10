""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time
import requests

from collections import deque

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from cowpy import cow

from userbot import CMD_HELP,YOUTUBE_API_KEY
from userbot.system import register

# ================= CONSTANT =================

NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
     "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Sharam kar bsdwale,kitni bkchodi deta.`",
    "`Chup Madarhox, bilkul chup..`",
    "`Me zindagi me chunotiyo se jyda inn jese Chutiyo se pareshaan hu.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`Jaana chodu chad jake land chaat`",
    "`Yaar ajab tere nkhare,gazab tera style hain, gand dhone ki tameez nahi, haath main mobile hai`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNSREACTS = [
    "`Runs far, far away from earth`",
    "`Running faster than supercomputer, cuzwhynot`",
    "`ZZzzZZzz... Huh? what? oh, just them again, nevermind.`",
    "Don't leave me alone with them!!",
    "`You run, you die.`",
    "`Jokes on you, I'm everywhere`",
    "You could also try /kickme, I hear that's fun.",
    "I'm behind you...",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Famous last words.",
    "Yeah yeah, just tap /kickme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Keep it up, not sure we want you here anyway.",
    "Hasta la vista, baby.",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
]

RAPE_STRINGS = [
     "`Rape Done Drink The Cum`",
     "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",
     "`The user has been successfully raped`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
     "`Rape coming... Raped! haha 😆`",
     "`Kitni baar Rape krvyega mujhse?`",
     "`Tu Randi hai Sabko pta hai😂`",
     "`Don't rape too much bossdk, else problem....`",
     "`Tu sasti rendi hai Sabko pta hai😂`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 
ABUSE_STRINGS = [
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Muh Me Lega Bhosdike ?`",
	   "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",
       "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
       "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
       "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",
       "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Proness Lebel: 6969696969`",
     "`Itna pro banda dekhlia bc, ab to marna hoga.`",
     "`U iz pro but i iz ur DAD, KeK`",
     "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
     "`Sometimes one middle finger isnâ€™t enough to let someone know how you feel. Thatâ€™s why you have two hands`",
     "`Some Nimbas need to open their small minds instead of their big mouths`",
     "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
     "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
     "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",

]
CHU_STRINGS = [
     "`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
     "`jindagi ki na toote lari iski lulli hoti nhi khadi`",
     "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
     "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
     "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
     "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
     "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
]
FUK_STRINGS = [
   "`It's better to let someone think you are an Idiot than to open your mouth and prove it.`",
   "`Talking to a liberal is like trying to explain social media to a 70 years old`",
   "`CHAND PE HAI APUN LAWDE.`",
   "`Pehle main tereko chakna dega, fir daru pilayega, fir jab aap dimag se nahi L*nd se sochoge, tab bolega..`",
   "`Pardhan mantri se number liya, parliament apne :__;baap ka hai...`",
   "`Cachaa Ooo bhosdi wale Chacha`",
   "`Aaisi Londiya Chodiye, L*nd Ka Aapa Khoye, Auro Se Chudi Na Ho, Biwi Wo Hi Hoye`",
   "`Nachoo Bhosdike Nachoo`",
   "`Jinda toh jaat ke baal bhi hai`",
   "`Sab ko pta tu randi ka baccha hai (its just a joke)`", 
]
THANOS_STRINGS = [
     "`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
     "`Pani kam hai matkey me ga*d mardunga teri ek jatke me`",
     "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
     "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
     "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
     "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
     "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
     "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
     "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
     "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]
ABUSEHARD_STRING = [
	"`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
	"`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
	"`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
    "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
    "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
    "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
    "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
    "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
    "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
	"`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
]
SHGS = [
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "ლ(ﾟдﾟლ)",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "ლ｜＾Д＾ლ｜",
    "ლ（╹ε╹ლ）",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    "¯\_(ツ)_/¯",
    "¯\_(⊙_ʖ⊙)_/¯",
]
CRI = [
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "(;Д;)",
    "（>﹏<）",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(つд⊂)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
]
SLAP_TEMPLATES = [
    "{hits} {victim} with a {item}.",
    "{hits} {victim} in the face with a {item}.",
    "{hits} {victim} around a bit with a {item}.",
    "{throws} a {item} at {victim}.",
    "grabs a {item} and {throws} it at {victim}'s face.",
    "launches a {item} in {victim}'s general direction.",
    "starts slapping {victim} silly with a {item}.",
    "pins {victim} down and repeatedly {hits} them with a {item}.",
    "grabs up a {item} and {hits} {victim} with it.",
    "ties {victim} to a chair and {throws} a {item} at them.",
    "gave a friendly push to help {victim} learn to swim in lava."
]
ITEMS = [
    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
]
THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls",
]
HIT = [
    "hits",
    "whacks",
    "fek ke maari",
    "slaps",
    "smacks",
    "bashes",
]

# ===========================================


@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")

@register(outgoing=True, pattern="^:/$")
async def kek(keks):
    if not keks.text[0].isalpha() and keks.text[0] not in ("/", "#", "@", "!"):
        """ Check yourself ;)"""
        uio = ["/", "\\"]
        for i in range(1, 15):
            time.sleep(0.3)
            await keks.edit(":" + uio[i % 2])

@register(outgoing=True, pattern=r"^.coinflip (.*)")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        if event.fwd_from:
            return
        r = random.randint(1, 100)
        input_str = event.pattern_match.group(1)
        if input_str:
            input_str = input_str.lower()
        if r % 2 == 1:
            if input_str == "heads":
                await event.edit("The coin landed on: **Heads**.\nYou were correct.")
            elif input_str == "tails":
                await event.edit("The coin landed on: **Heads**.\nYou weren't correct, try again ...")
            else:
                await event.edit("The coin landed on: **Heads**.")
        elif r % 2 == 0:
            if input_str == "tails":
                await event.edit("The coin landed on: **Tails**.\nYou were correct.")
            elif input_str == "heads":
                await event.edit("The coin landed on: **Tails**.\nYou weren't correct, try again ...")
            else:
                await event.edit("The coin landed on: **Tails**.")
        else:
            await event.edit("Gimme another coin, this one fake AF !!")

@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        """ slaps a user, or get slapped if not a reply. """
        if event.fwd_from:
            return

        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id

        if not message_id_to_reply:
            message_id_to_reply = None

        try:
            await event.edit(caption)

        except:
            await event.edit("`Can't slap this person, need to fetch some sticks and stones !!`")

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None

    return replied_user

async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = "..." + temp.format(victim=slapped, item=item, hits=hit, throws=throw)

    return caption

@register(outgoing=True, pattern="^-_-$")
async def lol(lel):
    if not lel.text[0].isalpha() and lel.text[0] not in ("/", "#", "@", "!"):
        """ Ok... """
        okay = "-_-"
        for _ in range(10):
            okay = okay[:-1] + "_-"
            await lel.edit(okay)


@register(outgoing=True, pattern="^;_;$")
async def fun(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = ";__;"
        for __ in range(10):
            t = t[:-1] + "_;"
            await e.edit(t)

@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(CRI))

@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(INSULT_STRINGS))

@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 🅱️
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await cp_e.edit(reply_text)

			  
@register(outgoing=True, pattern="^.bt$")
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await bte.edit(
                "`BLUETEXT MUST CLICK.`\n"
                "`Are you a stupid animal which is attracted to colours?`"
            )

@register(outgoing=True, pattern="^.rape$")
async def raping (raped):
    """ Dont Rape Too much -_-"""
    if not raped.text[0].isalpha() and raped.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(RAPE_STRINGS) - 1)
        reply_text = RAPE_STRINGS[index]
        await raped.edit(reply_text)
			  
@register(outgoing=True, pattern="^.pro$")
async def proo (pros):
    """ String for Pros only -_-"""
    if not pros.text[0].isalpha() and pros.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(PRO_STRINGS) - 1)
        reply_text = PRO_STRINGS[index]
        await pros.edit(reply_text)

@register(outgoing=True, pattern="^.fuk$")
async def fhu (fuks):
    """ String for fhu only -_-"""
    if not fuks.text[0].isalpha() and fuks.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = FUK_STRINGS[index]
        await fuks.edit(reply_text)

@register(outgoing=True, pattern="^.chu$")
async def chutiya (chus):
    """ String for Chu only -_-"""
    if not chus.text[0].isalpha() and chus.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = CHU_STRINGS[index]
        await chus.edit(reply_text)
			  			  
@register(outgoing=True, pattern="^.thanos$")
async def thanos (thanos):
    """ String for thanos only -_-"""
    if not thanos.text[0].isalpha() and thanos.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(THANOS_STRINGS) - 1)
        reply_text = THANOS_STRINGS[index]
        await thanos.edit(reply_text)	
			  
@register(outgoing=True, pattern="^.abusehard$")
async def fuckedd (abusehard):
    """ Dont Use this Too much bsdk -_-"""
    if not abusehard.text[0].isalpha() and abusehard.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSEHARD_STRING) - 1)
        reply_text = ABUSEHARD_STRING[index]
        await abusehard.edit(reply_text)
			  			  
@register(outgoing=True, pattern="^.abuse$")
async def abusing (abused):
    """ Dont Abuse Too much bsdk -_-"""
    if not abused.text[0].isalpha() and abused.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSE_STRINGS) - 1)
        reply_text = ABUSE_STRINGS[index]
        await abused.edit(reply_text)

@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await owo.edit("` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await owo.edit(reply_text)

@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in ("/", "#", "@", "!"):
        await react.edit(random.choice(FACEREACTS))

@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(random.choice(SHGS))

@register(outgoing=True, pattern="^.runs$")
async def runner_lol(run):
    """ Run, run, RUNNN! """
    if not run.text[0].isalpha() and run.text[0] not in ("/", "#", "@", "!"):
        await run.edit(random.choice(RUNSREACTS))

@register(outgoing=True, pattern="^.oof$")
async def Oof(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = "Oof"
        for j in range(15):
            t = t[:-1] + "of"
            await e.edit(t)

@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)

@register(outgoing=True, pattern="^.smk (.*)")
async def smrk(smk):
        if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
            textx = await smk.get_reply_message()
            message = smk.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        if message == 'dele':
            await smk.edit( message +'te the hell' + "ツ" )
            await smk.edit("ツ")
        else:
             smirk = " ツ"
             reply_text = message + smirk
             await smk.edit(reply_text)


@register(outgoing=True, pattern=r".yt_dl (\S*) ?(\S*)")
async def download_video(v_url):
    """ For .yt_dl command, download videos from YouTube. """
    if not v_url.text[0].isalpha() and v_url.text[0] not in ("/", "#", "@", "!"):
        url = v_url.pattern_match.group(1)
        quality = v_url.pattern_match.group(2)

        await v_url.edit("**Fetching...**")

        video = YouTube(url)

        if quality:
            video_stream = video.streams.filter(
                progressive=True,
                subtype="mp4",
                res=quality
            ).first()
        else:
            video_stream = video.streams.filter(
                progressive=True,
                subtype="mp4"
            ).first()

        if video_stream is None:
            all_streams = video.streams.filter(
                progressive=True,
                subtype="mp4"
            ).all()
            available_qualities = ""

            for item in all_streams[:-1]:
                available_qualities += f"{item.resolution}, "
            available_qualities += all_streams[-1].resolution

            await v_url.edit(
                "**A stream matching your query wasn't found. Try again with different options.\n**"
                "**Available Qualities:**\n"
                f"{available_qualities}"
            )
            return

        video_size = video_stream.filesize / 1000000

        if video_size >= 50:
            await v_url.edit(
                ("**File larger than 50MB. Sending the link instead.\n**"
                 f"Get the video [here]({video_stream.url})\n\n"
                 "**If the video plays instead of downloading, right click(or long press on touchscreen) and "
                 "press 'Save Video As...'(may depend on the browser) to download the video.**")
            )
            return

        await v_url.edit("**Downloading...**")

        video_stream.download(filename=video.title)

        url = f"https://img.youtube.com/vi/{video.video_id}/maxresdefault.jpg"
        resp = get(url)
        with open('thumbnail.jpg', 'wb') as file:
            file.write(resp.content)

        await v_url.edit("**Uploading...**")
        await v_url.client.send_file(
            v_url.chat_id,
            f'{safe_filename(video.title)}.mp4',
            caption=f"{video.title}",
            thumb="thumbnail.jpg"
        )

        os.remove(f"{safe_filename(video.title)}.mp4")
        os.remove('thumbnail.jpg')
        await v_url.delete()
