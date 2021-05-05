from keep_alive import keep_alive
import discord
import os

client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hello Sam'):
    await message.channel.send('Hello!')
  
  if message.content.startswith('How are you Sam?'):
    await message.channel.send('I am fine wbu?')  
keep_alive()    
client.run(os.getenv('TOKEN'))
