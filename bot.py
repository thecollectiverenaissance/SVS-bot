import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

token = 'NzI3OTQwOTM5ODU0NjQzMjcx.XvztUQ.V1zGfRXW5IMaSGW4CFtOFeHokmU'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def ping(ctx):
    r = requests.get('https://discord.com/invite/ZqTBnzA')
    soup = BeautifulSoup(r.content, "html.parser")
    image = soup.find("meta",  property="og:image")["content"]
    await ctx.send(image)

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
