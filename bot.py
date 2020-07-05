import discord
import os
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

token = os.environ['BOT_TOKEN']
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def apply(ctx):
    await ctx.author.send('DM')

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
