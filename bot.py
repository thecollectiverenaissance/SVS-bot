import discord
import os
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

token = 'NzEwNjk3MTE4NDE0OTI5OTUw.XwFOFA.CB-LwJim7OBKIN92lGJK9qZFLUY'
client = commands.Bot(command_prefix = '%')
questions = ['What is your Server\'s Name?',
    'Please give a brief Description of your Server.',
    'Please provide an invite link, or if Private, a message you\'d like displayed in place of it.',
    'Please provide a link to your server image.']

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):
    start_embed = discord.Embed(
        description = 'Application Started - Type ".cancel" to cancel the application',
        colour = discord.Colour.blurple()
    )
    responces = []
    if message.content.startswith('.apply'):
        channel = message.author

        for i in questions:
            question_embed = discord.Embed(
                description = i,
                colour = discord.Colour.blurple()
            )
            await channel.send(embed=question_embed)

            def check(m):
                if m.author == channel:
                    responces.append(m.content)
                return m.author == channel

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

client.run(token)
