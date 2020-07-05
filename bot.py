import discord
import os
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

token = os.environ['BOT_TOKEN']
client = commands.Bot(command_prefix = '.')
questions = ['What is your Server\'s Name?',
    'Please give a brief Description of your Server.',
    'Please provide an invite link, or if Private, a message you\'d like displayed in place of it.',
    'Please provide a link to your server image.']

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def apply(message):
    start_embed = discord.Embed(
        description = 'Application Started - Type ".cancel" to cancel the application',
        colour = discord.Colour.blurple()
    )
    responces = []
    channel = message.author

    for i in questions:
        question_embed = discord.Embed(
            description = i,
            colour = discord.Colour.blurple()
        )
        await channel.send(embed=question_embed)

        def check(m):
            if m.author == channel and isinstance(m.channel, discord.channel.DMChannel):
                responces.append(m.content)
            return m.author == channel and isinstance(m.channel, discord.channel.DMChannel)

        msg = await client.wait_for('message', check=check)
    await channel.send('**Your application has been submitted!**')
    responce_channel = client.get_channel(556614414153809963)
    print(responces)

    try:
        r = requests.get(responces[2])
        soup = BeautifulSoup(r.content, "html.parser")
        image = soup.find("meta",  property="og:image")["content"]
    except:
        image = 'N/A'

    responce_embed = discord.Embed(
        description = f"\n{questions[0]} -\n{responces[0]}\n{questions[1]} -\n{responces[1]}\n{questions[2]} -\n{responces[2]}\n{questions[3]} -\n{responces[3]}\nServer Image (taken from invite) -\n{image}",
        colour = discord.Colour.blurple()
    )

    await responce_channel.send(embed=responce_embed)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def info(ctx, name, desc, invite, icon):
    embed = discord.Embed(
        title = name,
        description = desc,
        colour = discord.Colour.blurple()
    )

    if icon != '':
        embed.set_thumbnail(url=icon)
    if invite != '':
        embed.add_field(name='Server Invite', value=invite, inline=False)

    await ctx.send(embed=embed)

@client.command()
async def hof(ctx, title,desc,ep,art,single):
    embed = discord.Embed(
        title = title,
        description = desc,
        colour = discord.Colour.gold()
    )
    embed.add_field(name='Best Overall EP', value=ep, inline=False)
    embed.add_field(name='Best Cover Art', value=art, inline=False)
    embed.add_field(name='Best Single', value=single, inline=False)

    await ctx.send(embed=embed)

    
@client.command()
async def list(ctx, title,*eps):
    print(eps)

client.run(token)
