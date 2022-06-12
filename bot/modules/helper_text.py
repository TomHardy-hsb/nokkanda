import pickle
import shutil, psutil
import time
from os import execl
from sys import executable
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import Message
from bot import (
    botStartTime,
    AUTHORIZED_CHATS,
    OWNER_ID
)
import bot.helper.ext_utils.fs_utils
from bot.helper.ext_utils import fs_utils
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from bot.helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time


@Client.on_message(
    filters.command(BotCommands.StatsCommand) &
    filters.chat(AUTHORIZED_CHATS)
)
def stats(client: Client, message: Message):
    currentTime = get_readable_time((time.time() - botStartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    netio = psutil.net_io_counters()
    sent = netio[0]
    recieved = netio[1]
    stats = f'<b>Bot Uptime</b>: {currentTime}\n' \
            f'<b>Total Disk space</b>: {total}\n' \
            f'<b>Used</b>: {used}\n' \
            f'<b>Free</b>: {free}\n' \
            f'<b>CPU</b>: {cpuUsage}%\n' \
            f'<b>RAM</b>: {memory}%\n' \
            f"<b>Sent</b>: {get_readable_file_size(sent)}\n" \
            f"<b>Recieved</b>: {get_readable_file_size(recieved)}" 
    sendMessage(stats, client, message)


@Client.on_message(
    filters.command(BotCommands.StartCommand) &
    filters.chat(AUTHORIZED_CHATS)
)
def start(client: Client, message: Message):
    start_string = start_string = f'''
Ya! I'm Alive Send A Magnet/.torrent/Https Link
'''
    sendMessage(start_string, client, message)


@Client.on_message(
    filters.command(BotCommands.RestartCommand) &
    filters.user(OWNER_ID)
)
def restart(client: Client, message: Message):
    restart_message = sendMessage(
        "Restarting, Please wait!",
        client,
        message
    )
    # Save restart message object in order to reply to it after restarting
    fs_utils.clean_all()
    with open('restart.pickle', 'wb') as status:
        pickle.dump(restart_message, status)
    execl(executable, executable, "-m", "bot")


@Client.on_message(
    filters.command(BotCommands.PingCommand) &
    filters.chat(AUTHORIZED_CHATS)
)
def ping(client: Client, message: Message):
    start_time = int(round(time.time() * 1000))
    reply = sendMessage("Starting Ping", client, message)
    end_time = int(round(time.time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)


@Client.on_message(
    filters.command(BotCommands.LogCommand) &
    filters.user(OWNER_ID)
)
def log(client: Client, message: Message):
    sendLogFile(client, message)


