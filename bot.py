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
application_start_message = ''
application_end_message = '**Your application has been submitted!**'

async def server_embed(ctx, name, desc, invite, icon):
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
    await channel.send(application_end_message)
    responce_channel = client.get_channel(728359983854649474)
    print(responces)

    try:
        r = requests.get(responces[2])
        soup = BeautifulSoup(r.content, "html.parser")
        image = soup.find("meta",  property="og:image")["content"]
    except:
        image = 'N/A'

    responce_embed = discord.Embed(
        title = responces[0],
        description = responces[1],
        colour = discord.Colour.blurple()
    )

    if responces[2] != '':
        responce_embed.add_field(name='Server Invite', value=responces[2], inline=False)
    if responces[3] != '':
        responce_embed.add_field(name='Image from Survey', value=responces[3], inline=False)
    responce_embed.add_field(name='Image from Invite', value=image, inline=False)
    responce_embed.add_field(name='', value='React with ✅ to use survey image. React with ☑️ to use invite image. React with 🔴 to deny form.', inline=True)

    #Mod verification surey should be posted
    react_msg = await responce_channel.send(embed=responce_embed)
    competing_servers = client.get_channel(727977909540880475)
    await react_msg.add_reaction("✅")
    await react_msg.add_reaction("☑️")
    await react_msg.add_reaction("🔴")

    def reaction_check(reaction, user):
        return user == message.author and str(reaction.emoji) in ['✅','☑️','🔴']

    reaction, user = await client.wait_for('reaction_add', check=reaction_check)
    if(reaction.emoji == '✅'):
        await server_embed(competing_servers, responces[0], responces[1], responces[2], responces[3])
    if(reaction.emoji == '☑️'):
        await server_embed(competing_servers, responces[0], responces[1], responces[2], image)
    if(reaction.emoji == '🔴'):
        await responce_channel.send('Form Denied')

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
async def listlinks(ctx, title,desc,*eps):
    
    embed = discord.Embed(
        title = title,
        description = desc,
        colour = discord.Colour.gold()
    )
    
    for i in range(0,len(eps),2):
        embed.add_field(name=eps[i], value=eps[i+1], inline=False)       

    await ctx.send(embed=embed)
client.run(token)
