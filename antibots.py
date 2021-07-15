import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

# --------------------------------------------- #
#    This code isn't meant to be stylish        #
#   but to work properly and be efficient       #
#    for issues open a ticket on github         #
# --------------------------------------------- #

bot_token = "INSERT BOT TOKEN HERE"  # Can be retrieved from @BotFather on telegram.
api_hash = "INSERT API HASH HERE"  # Can be retrieved when creating a new application from telegram.org
api_id = "INSERT API ID HERE << AS INTEGER (REMOVE QUOTATION MARKS) >>"  # Can be retrieved when creating a new application from telegram.org

app = Client("antibot", bot_token=bot_token, api_id=api_id, api_hash=api_hash)  # Do not modify any of this.

voips = []
suspicious = []
channelid = 0


async def ownership(cid, uid):
    try:
        member = await app.get_chat_member(cid, uid)
        if member.status in ["administrator", "creator"]:
            return True
        else:
            return False
    except:
        return False


@app.on_message(filters.private & filters.command(commands=['start'], prefixes=['/'], case_sensitive=False))  # Add commands or prefixes as a list.
async def start(client: Client, message: Message) -> int:
    global voips
    global suspicious
    global channelid

    suspicious.clear()
    voips.clear()

    channelid = message.command[1]
    count = 0
    if channelid.startswith("-100"):
        if await ownership(channelid, message.from_user.id):
            async for member in client.iter_chat_members(channelid):  # Telegram has a limit of 200 members for each call, do the command more times to remove additional VoIPs
                count += 1
                if member.user.dc_id in [1, 3, 5]:
                    voips.append(member.user.id)
                if member.user.dc_id in [2, None]:
                    suspicious.append(member.user.id)
            await client.send_message(message.chat.id, f"There are {len(voips)} VoIPs & {len(suspicious)} suspicious accounts on a {count} members scan.")
        else:
            await client.send_message(message.chat.id, "You're not an administrator of this channel or the bot isn't admin yet.")
    else:
        await client.send_message(message.chat.id, "The channel ID that you provided isn't correct.")

    return 0


@app.on_message(filters.private & filters.command(commands=['remove'], prefixes=['/'], case_sensitive=False))
async def removal(client: Client, message: Message) -> bool:
    global channelid
    global voips
    global suspicious

    try:
        if message.command[1] == "1":
            for x in voips:
                await client.kick_chat_member(channelid, x)
            await client.send_message(message.chat.id, f"Successfully kicked all VoIPs.")
            voips.clear()
        elif message.command[1] == "2":
            for x in voips:
                await client.kick_chat_member(channelid, x)
            for y in suspicious:
                await client.kick_chat_member(channelid, y)
            await client.send_message(message.chat.id, f"Successfully kicked all VoIPs and Suspicious Accounts.")
            voips.clear()
            suspicious.clear()
    except FloodWait as e:
        await client.send_message(message.chat.id, f"Bot is now in a floodwait of {e.x} seconds.")
        await asyncio.sleep(e.x)

    return True

app.run()
