import discord
from discord.ext import commands,tasks
import os




import requests
import json
import random

import bs4

client = discord.Client()


def get_character():
  response = requests.request('https://jikan1.p.rapidapi.com/character/1/pictures')
  json_data = json.loads(response.text)
  character = json_data[0]['']

@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
   if message.author == client.user:
     return

   if message.content.startswith('`newc'):
     character = get_character()
     await message.channel.send('character')

@client.event
async def on_message(message):
 if message.author == client.user:
    return

 if message.content.startswith('k'):
  await message.channel.send('Shut up!')






  
client.run(os.getenv('TOKEN'))