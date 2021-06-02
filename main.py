import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

upset_words=["dhurr","bhallagchena","eta ki hocche",
"sick",":')","bt","darjeeling","sad","angry","ughh","nooooo","uff"]

starter_enc=[
  "cheer up",
  "hang in there",
  "you will feel better",
  "can I offer you a hot beverage?",
  "grab a smoke,maybe?"
  "meow"
]

def get_quote():
 
 response=requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
 quote=response.text
 return(quote)


 

@client.event
async def on_ready():
  print('succesfully logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg=message.content

  if msg.startswith('*inspire'):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in upset_words):
    await message.channel.send(random.choice(starter_enc))


keep_alive()
client.run( os.environ['TOKEN'])

