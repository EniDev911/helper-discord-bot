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
from utilities.settings import DISCORD
from utilities.searcher import *

# intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", description="Este es un bot creado por EniDev911")

DiscordComponents(bot)

# GLOBAL
BASE_DIR = os.path.dirname(__file__)

# get youtube
@bot.command()
async def yt(ctx, *, search):
	await ctx.send(youtube(search))

# get google font
# @bot.command()
# async def gf(ctx, *, font):
# 	await ctx.send(google_font())


@bot.command()
async def emb(ctx):
	embed = discord.Embed(
		title = 'Codepen',
		description = 'Open in codepen',
		url = 'https://codepen.io/EniDev911/pen/jOzVzeK',
		timestamp=datetime.datetime.utcnow(),
		color=blue
		)
	embed.set_footer(text='This is a footer')
	embed.set_image(url='https://badges.aleen42.com/src/codepen.svg')
	embed.set_thumbnail(url='https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/96/000000/external-multi-platform-online-code-editor-and-open-source-learning-service-logo-shadow-tal-revivo.png')
	embed.set_author(name='Codepen', icon_url='https://blog.codepen.io/wp-content/uploads/2012/06/Button-Fill-Black-Large.png')
	embed.add_field(name='Field name', value='Field value', inline=False)
	embed.add_field(name='Field name', value='Field value', inline=True)
	embed.add_field(name='Field name', value='Field value', inline=True)

	await ctx.send(embed=embed)



@bot.command()
async def playlist(ctx):
	channel = discord.utils.get(ctx.guild.channels, name="hydra-song-requests")
	#channel = bot.get_channel(int(channel.id))
	#await channel.send("pokemon")
	
	await bot.get_channel(int(channel.id)).send("play pokemon", file=discord.File(os.path.join(BASE_DIR,"img")+"/logo_con_bg.png"))
	# print(os.path.join(BASE_DIR, "img")+"/logo_con_bg.png")
	await ctx.send(ctx.guild.name)
	



@bot.event
async def on_select_option(interaction):
	if interaction.values[0] == "prompt":
		print("prompt")
    
	await interaction.respond(content=f"{interaction.values[0]} selected!") 

# ===== read document
def read(document: str):

	with open(os.path.join(BASE_DIR+'/papers', document) ,'r', encoding='utf-8') as file:
		file_clean = ""
		for readline in file:
			line_strip = readline.lstrip("\n")
			file_clean += line_strip
		return file_clean
	

# ==== show examples
@bot.command()
async def ejemplo(ctx, *, search: str):
	result = search.strip()
	try:
		file = read('js/'+result+'.md')
		await ctx.send(file)

	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 

@bot.command()
async def font(ctx, *, search: str):
	result = search.strip()
	try:
		file = read('fonts/'+result.lower()+'.md')
		await ctx.send(file)

	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 



async def get_embed():
	embed = discord.Embed(
		title = 'Title',
		description = 'This is a description',
		timestamp=datetime.datetime.utcnow(),
		color=0xf9f06b
	)
	embed.set_footer(text='This is a footer')
	embed.set_image(url='https://raw.githubusercontent.com/EniDev911/enidev911_guides/main/assets/png/prompt.png')
	embed.set_thumbnail(url='https://raw.githubusercontent.com/EniDev911/enidev911_guides/main/assets/png/prompt.png')
	embed.set_author(name='EniDev911', icon_url='https://avatars.githubusercontent.com/u/70834807?v=4')
	embed.add_field(name='Field name', value='Field value', inline=False)
	embed.add_field(name='Field name', value='Field value', inline=True)
	embed.add_field(name='Field name', value='Field value', inline=True)
	return embed



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
	print("My boot is Ready")

if __name__ == "__main__":
	#e = Embed("hello", "description", None, 0x1f6e9e)
	print(youtube("hello"))
	print(DISCORD["version"])
	load_dotenv(find_dotenv())
	bot.run(os.environ["DISCORD_TOKEN"])
