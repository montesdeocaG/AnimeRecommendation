import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
import random

#token del bot, muy importante no revelar. confidencial.
TOKEN = 'TOKEN GOES HERE'

client = discord.Client()

#lista de imagenes de conejos, en una función
def conejorandom():
    con = [r'C:\Users\Saulo\Desktop\discordbot\conejo0.jpg', r'C:\Users\Saulo\Desktop\discordbot\conejo1.jpg', r'C:\Users\Saulo\Desktop\discordbot\conejo2.jpg', r'C:\Users\Saulo\Desktop\discordbot\conejo3.jpg', r'C:\Users\Saulo\Desktop\discordbot\conejo4.jpg']
    return random.choice(con)

@client.event
async def on_message(msg):
    #para que el bot no se responda solo...
    if msg.author == client.user:
        return

    #todos los ifs son respuestas a mensajes, usar el mismo formato para añadir más.
    msg.content = msg.content.lower()
    if msg.content == ('$hola'):
        # la respuesta menciona la usuario que llamó al bot)
        await msg.channel.send('Qué hubo, {0.author.mention}?'.format(msg))

    if msg.content == ('conejo'):
        #utilizando la funcion conejo y la lista de imagenes, postea una random al detecta el comando
        await msg.channel.send(file=discord.File(conejorandom()))

    #reacciona con un emoji al detectar la palabra clave.
    emoji = '\N{THUMBS UP SIGN}'
    if msg.content == ('chale'):
        await msg.add_reaction(emoji)

@client.event
async def on_ready():
    #el bot está "haciendo" esto según Discord, se puede cambiar a otra actividad.
    activity = discord.Activity(name='with your feelings', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    #para confirmar que el bot funcione
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('TOKEN GOES HERE')

