#---------------------------------------
#        Module: index										
#        Author: Marco Contreras		
#         Email: enidev911@gmail.com 				
#---------------------------------------

from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands
from discord_components import (
	DiscordComponents, 
	Select, 
	SelectOption
)
import asyncio
import os
import datetime 
from urllib import parse, request
import webbrowser
from utilities.settings import DISCORD, BASE_DIR
from utilities.formatter import format_text, format_url
from utilities.components.embed import *
from utilities.components.button import *
from utilities.searcher import *
from utilities.files import read, read_as_dict
from colorama import Fore

# intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", description="Este es un bot creado por EniDev911")

# ready 
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Un comando"))
	print(f"{Fore.YELLOW}Bot logged as {Fore.RED}{bot.user}")

# get youtube
@bot.command(name="yt")
async def youtube(ctx, *, search):
	await ctx.send(youtube_search(search))

# get google
@bot.command(name="gg")
async def google(ctx, *, search:str):
	await ctx.send(f"⚓ {google_search(search)}")

# get font-awesome 
@bot.command(name="fa")
async def font_awesome(ctx, *, search=""):
	result = read_as_dict("fa6/icons",search)
	if "👻" in result:
		await ctx.send(format_text(result, "fix"))
		return

	await ctx.send(format_text(result, "html"))
	await btn_clipboard(bot, ctx,result)

# get google-fonts
@bot.command(name="gf")
async def google_font(ctx, *, search=""):
	result = read_as_dict('ggfonts/fonts',search)
	rule = read_as_dict('ggfonts/rules',search)
	if "👻" in result:
		await ctx.send(format_text(result, "fix"))
		return
		
	await ctx.send(format_text(format_url(result, rule, "css"),"css"))
	await btn_clipboard(bot, ctx,format_url(result, rule, "css"))

# get js references
@bot.command(name="js")
async def javascript(ctx, *, search: str):
		file = read('js/'+search)
		await ctx.send(file)


# get python references
@bot.command(name="python")
async def python(ctx, *, search: str):
	result = read_as_dict("fa6/icons",search)

	

# get boostrap references
@bot.command(name="bs")
async def bootstrap(ctx, *, search: str):
		file = read('bs/'+search)
		await ctx.send(file)



@bot.command(name="info")
async def info_server(ctx):

	await ctx.send('https://raw.githubusercontent.com/EniDev911/assets/main/png/logo/logo_con_bg.png')
	await ctx.send(embed=info(ctx))


@bot.command()
async def playlist(ctx):
	channel = discord.utils.get(ctx.guild.channels, name="hydra-song-requests")
	#channel = bot.get_channel(int(channel.id))
	
	await bot.get_channel(int(channel.id)).send("play pokemon", file=discord.File(os.path.join(BASE_DIR,"img")+"/logo_con_bg.png"))
	# print(os.path.join(BASE_DIR, "img")+"/logo_con_bg.png")
	await ctx.send(ctx.guild.name)
	

@bot.command()
async def ping(ctx):
	await ctx.send(format_text(f"🏓 pong con {str(round(bot.latency, 2))} de latencia", "fix"))



if __name__ == "__main__":
	print(DISCORD["version"])
	load_dotenv(find_dotenv())
	DiscordComponents(bot)
	bot.run(os.environ["DISCORD_TOKEN"])
