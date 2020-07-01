import discord
from discord.ext import commands

token = 'NzI3OTQwOTM5ODU0NjQzMjcx.XvzJ2Q.SlM-ith3Nzz02qVVad2qWXsv-rE'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def info(ctx, name, desc, invite, icon):
    embed = discord.Embed(
        title = name,
        description = desc,
        colour = discord.Colour.blue()
    )

    embed.set_thumbnail(url=icon)
    embed.add_field(name='Server Invite', value=invite, inline=False)

    await ctx.send(embed=embed)

client.run(token)
