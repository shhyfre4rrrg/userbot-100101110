from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd("menziona (.*)"))
async def _(event):
	if event.fwd_from:
		return	
	input_str = event.pattern_match.group(1)
	if event.reply_to_msg_id:
		previous_message = await event.get_reply_message()
		if previous_message.forward:
			replied_user = previous_message.forward.from_id
		else:
			replied_user = previous_message.from_id
	else:
		await event.edit("rispondi ad un messaggio")
	user_id = replied_user
	caption = """<a href='tg://user?id={}'>{}</a>""".format(user_id, input_str)
	await event.edit(caption, parse_mode="HTML")
