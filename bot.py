import os
import random

import discord
import webscraper
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='check_stock', help='Check stock from apple store.')
async def check_stock(ctx):
    result = webscraper.check_stock()
    if (result):
        await ctx.send('OUT OF STOCK!')
    else:
        await ctx.send('IN STOCK!')

bot.run(TOKEN)

# @client.event
# async def on_ready():
#     guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
#     print(
#         f'{client.user} has connected to Discord!'
#         )

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday!')
#     if 'check stock' in message.content.lower():
#         await message.channel.send()

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

# client.run(TOKEN)