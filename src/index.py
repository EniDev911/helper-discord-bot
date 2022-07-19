#---------------------------------------
#        Module: main										
#        Author: Marco Contreras		
#         Email: enidev911@gmail.com 	
# 										
#     Copyright: (c) EniDev911			
#       Licence: GPL 3.0 				
#---------------------------------------

from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands
from discord_components import (
	Button, 
	ButtonStyle,
	DiscordComponents, 
	Select, 
	SelectOption
)
import asyncio
import os
import datetime 
from urllib import parse, request
import re
import webbrowser
from utilities.colors import * 
from utilities.settings import DISCORD, BASE_DIR
from utilities.components.embed import *
from utilities.searcher import *
from utilities.files import read
from colorama import Fore

# intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", description="Este es un bot creado por EniDev911")

DiscordComponents(bot)

# get youtube
@bot.command()
async def yt(ctx, *, search):
	await ctx.send(youtube(search))

# get fonts
@bot.command()
async def font(ctx, *, search: str):
	result = search.strip().replace(" ", "")
	try:
		file = read('fonts/'+result.lower()+'.md')
		await ctx.send(file)
	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 

# get js references
@bot.command(name="js")
async def javascript(ctx, *, search: str):
	result = search.strip()
	try:
		file = read('js/'+result+'.md')
		await ctx.send(file)

	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 

# get boostrap references
@bot.command(name="bs")
async def bootstrap(ctx, *, search: str):
	result = search.strip()
	try:
		file = read('bs/'+result+'.md')
		await ctx.send(file)

	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 


@bot.command()
async def emb(ctx):
	# file = read('fonts/firacode.md')
	emb = embed_bootstrap
	#print(emb.to_dict())
	#discord.Embed.from_dict(embed_dict)
	await ctx.send(embed=emb)



@bot.command()
async def playlist(ctx):
	channel = discord.utils.get(ctx.guild.channels, name="hydra-song-requests")
	#channel = bot.get_channel(int(channel.id))
	
	await bot.get_channel(int(channel.id)).send("play pokemon", file=discord.File(os.path.join(BASE_DIR,"img")+"/logo_con_bg.png"))
	# print(os.path.join(BASE_DIR, "img")+"/logo_con_bg.png")
	await ctx.send(ctx.guild.name)
	



@bot.event
async def on_select_option(interaction):
	if interaction.values[0] == "prompt":
		print("prompt")
    
	await interaction.respond(content=f"{interaction.values[0]} selected!") 



# Events
# ==========
# Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Un comando"))
	print(f"{Fore.YELLOW}Bot logged as {Fore.RED}{bot.user}")

if __name__ == "__main__":
	e = Embed("hello", "description", None, 0x1f6e9e)
	print(e.to_dict())
	print(DISCORD["version"])
	load_dotenv(find_dotenv())
	bot.run(os.environ["DISCORD_TOKEN"])
