import discord
import random

client = discord.Client()

tokenFile = open(".token", "r")
TOKEN = tokenFile.read()
tokenFile.close()

phraselist = [
    'callese we',
    'Hugo me encanta',
    'Me la pones tiesaaaaaa Jugoooo',
    'El luis sela come jsjs',
    'Saquen el maicra',
    'pq?',
    'pq?',
    'pq?',
    'Aiudaaaaaaaaa me balasean los municipaleees',
    'kien pa un sereal?',
    'aiuda, me sineto sobrio',
    'rolame un tabaco o t quito la bida',
    'silensio',
    'jsjaja ese we',
    't amo',
    'quieres culiar?',
    'Mi hijo de 12 años (actualmente) una vez que íbamos a desayunar huevitos me dijo, hay mami estos huevitos huelen a la comidita que nos daba diosito cuando nos sentaba en una mesa larga larga a desayunar a todos los angelitos (casualidad? Mi hijo se llama ángel !)',
    'atras de tiii pana!',
    'si pudiera ser tu eroe, si pudiera ser tu dios y salbarte mil beses',
    'ajijuesu, yase ambre',
    'pa luego es tarde mi maicol',
    'jijuesumaicol jacson jsjsjaj ese we',
    'ando pachequito rasa, no ablen en ingles',
    'ctm pinche chairo puto',
    'jsjajaj Ramon',
    'cuming'
]

@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(random.choice(phraselist))

client.run(TOKEN)