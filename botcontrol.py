import discord
import termcolor
TOKEN = input(termcolor.colored('[#] Enter token: ', 'blue'))
client = discord.Client()
@client.event
async def on_ready():
 print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
 if message.author == client.user:
  return
 if message.content.startswith('/connect'):
  await message.channel.send('Connected')
  while True:
     msg = input(termcolor.colored('[#] Enter message: ', 'blue'))
     await message.channel.send(msg)
     print(termcolor.colored('[+] Message Successfully Sent', 'green'))
     print(termcolor.colored(('[*] Message: ' + msg), 'yellow'))
client.run(TOKEN)
