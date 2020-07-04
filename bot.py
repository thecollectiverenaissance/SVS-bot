import discord
from discord.ext import commands

token = os.environ['BOT_TOKEN']
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Ready!')

@client.command()
async def info(ctx, name, desc, invite, icon):
    embed = discord.Embed(
        title = name,
        description = desc,
        colour = discord.Colour.blurple()
    )

    embed.set_thumbnail(url=icon)
    embed.add_field(name='Server Invite', value=invite, inline=False)

    await ctx.send(embed=embed)

client.run(token)
