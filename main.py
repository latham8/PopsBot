from datetime import datetime, time

import discord
from discord.ext import commands
from tokens import *

## Production Token - Do not use for Development
##token = 'ODQzNjQ0MzkxMzY0ODg2NTM4.YKG3EQ.SyaBwtvx177TD9Xw9YLPGaohdF4'
##token = 'ODQzODk3Mjc4MDg2NjQzNzIy.YKKilQ.8Z0TySXiS8o6ZRT-Mj004SEaSWE'


client = commands.Bot(command_prefix = '.')
version = '1.2.3'

@client.event
async def on_ready():
    print('Bot has started!')
    discord.Activity(name="Making money, as always :smirk:", type=1)
""""
@client.event
async def on_message(message):
    if message.content.startswith('.'):
        cmd = (message.content + '. ').split('.')[1]  # finds everything after sm!
        embedVar = discord.Embed(title="Pops Crypto Callout")
        embedVar.add_field(name='Ticker', value='BTC', inline=False)
        embedVar.add_field(name='Long/Short', value='Long', inline=False)
        embedVar.add_field(name='Entry', value='10', inline=False)
        embedVar.add_field(name='Target', value='15', inline=False)
        await message.channel.send(embed=embedVar)
"""
@client.command(pass_context=True)
async def pops(cxt, ticker, pe, pt, sl, lev, *, comments=None):

    now = datetime.now() ## For time in footer
    time = now.strftime("%I:%M:%S %p") ## For time in footer
    embedVar = discord.Embed(title="**Pops Crypto Callout**", color=0x00FF00)
# Image at the bottom - using thumbnail instead    embedVar.set_image(url="https://cdn.discordapp.com/emojis/839112040681177118.png?v=1")
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/839112040681177118.png?v=1")
    embedVar.insert_field_at(index=(0),name='Ticker', value=ticker.upper(), inline=False)
    embedVar.insert_field_at(index=(1),name=f':green_square: Entry - {pe}', value='\n\u200b', inline=False)
    embedVar.insert_field_at(index=(2), name=f':white_check_mark: Target - {pt}', value='\u200b', inline=False)
    embedVar.add_field(name=f':x: Stop Loss - {sl}', value='\n\u200b', inline=False)
    embedVar.add_field(name=f':arrow_double_up: Leverage - {lev}', value='\u200b', inline=False)
    embedVar.add_field(name='Comments', value=comments, inline=False)
    embedVar.set_footer(text=f"- Latham.xyz - PopsBot v{version} - {time}")
    await cxt.channel.send(embed=embedVar)
    await cxt.message.delete()
@client.command(pass_context=True)
async def popscomment(cxt, comment):
    now = datetime.now() ## For time in footer
    time = now.strftime("%I:%M:%S %p") ## For time in footer

    embedVar = discord.Embed(title="Pop's Crypto", color=0xFFA500)
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/839112040681177118.png?v=1")
    embedVar.add_field(name='\n\u200b', value=comment)
    embedVar.set_footer(text=f"- Latham.xyz - PopsBot v{version} - {time}")

    await cxt.channel.send(embed=embedVar)
    await cxt.message.delete()

client.run(token)