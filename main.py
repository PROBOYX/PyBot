from telethon  import TelegramClient, events, Button

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '/',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def encode(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def decode(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())



def text(text):
    if text.startswith(".") or text.startswith("-"):
        decodeText = decode(text)
        return decodeText
    else:
        encodeText = encode(text)
        return encodeText

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
        await event.reply(str(text))


bot.run_until_disconnected()
