from telethon  import TelegramClient, events, Button
import morse_talk as mtalk


def text(text):
    if text.startswith(".") or text.startswith("-"):
        decode = mtalk.decode(text).plaintext
        return decode
    else:
        encode = mtalk.encode(text).morse
        return encode

api_id = 1621727
api_hash = "31350903c528876f79527398c09660ce"
token = "5627628015:AAHaCVsQ9o_cEhhdF1EayNCq2A-xXIX4Wzk"

bot = TelegramClient("morse", api_id, api_hash).start(bot_token=token)

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.respond("Forward/Send the text")

@bot.on(events.NewMessage(incoming=True))
async def translate(event):
    if event.text == "/start":
        pass
    else:
        text(event.text)
        print (text)
        await event.reply(text)


bot.run_until_disconnected()
