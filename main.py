# COPYRIGHT 2023 BY ULTRA X
from telethon  import TelegramClient, events, Button
import asyncio
import io
import os
import sys
import traceback


api_id = 1621727
api_hash = "31350903c528876f79527398c09660ce"
token = "5325238526:AAEcWx21slJatAOlPj-QuSWcNr-C58-vQYU"

bot = TelegramClient("morse", api_id, api_hash).start(bot_token=token)
xbot = bot
@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.respond("Yoo Im ready")




@xbot.on(events.NewMessage(pattern="/run ?(.*)"))
async def _(event):
    cmd = event.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await event.reply("What should I run ?..\n\nGive me something to run, u dumbo!!")
    proevent = await event.reply("Running.....")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sᴜᴄᴄᴇss ✅"
    final_output = f"**•  Eᴠᴀʟ : **\n`{cmd}` \n\n**•  Rᴇsᴜʟᴛ : **\n`{evaluation}` \n"
    await proevent.edit(final_output)


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )



@xbot.on(events.NewMessage(pattern="/exec ?(.*)"))
async def _(event):
    cmd = event.text.split(" ", maxsplit=1)[1]
    if not cmd:
        return await event.reply("What should I execute?..\n\nGive me somwthing to execute, u dumbo!!")
    proevent = await event.reply("Executing.....")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    curruser = "UltraX"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
    else:
        cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
    await proevent.edit(cresult)


bot.run_until_disconnected()
