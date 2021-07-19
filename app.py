import discord
import random
from Phrases import Phrases

def getToken(filename):
    tokenFile = open(filename, "r")
    token = tokenFile.read()
    tokenFile.close()
    return token

phrases = Phrases('phrases.txt')
client = discord.Client()

@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(phrases.getRandomPhrase())

client.run(getToken('.token'))