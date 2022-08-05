#---------------------------------------
#        Module: index										
#        Author: Marco Contreras		
#         Email: enidev911@gmail.com		
#---------------------------------------

from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands
from discord_components import DiscordComponents
import asyncio
import os
import datetime 
from urllib import parse, request
import webbrowser
from utilities.settings import DISCORD, BASE_DIR, API_KEY
from utilities.formatter import format_text, format_url
from utilities.components.embed import *
from utilities.components.button import *
from utilities.searcher import *
from utilities.files import read, read_as_dict
from colorama import Fore
from pexels_api import API
import pokebase as pb


# intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", description="Este es un bot creado por EniDev911")

# ready 
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Un comando (Ej:!fa discord)"))
	print(f"{Fore.YELLOW}Bot logged as {Fore.RED}{bot.user}")

# get youtube
@bot.command(name="yt")
async def youtube(ctx, *, search):
	await ctx.send(youtube_search(search))

# get page google
@bot.command(name="gg")
async def google(ctx, *, search:str):
	await ctx.send(f"⚓ {google_search(search)}")

# get pokemon pokebase
@bot.command(name="pb")
async def pokebase(ctx,*, search: str):
	#await ctx.send(pokemon.sprites.front_default)
	await ctx.send(embed=pokemon(ctx, search))

#s1.url
#'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png'
#s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
#s2.path
#'/home/user/.cache/pokebase/sprite/pokemon/other-sprites/official-artwork/1.png'
#s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
#s3.img_data

# get images pexels
@bot.command(name="pxl")
async def pexels(ctx, *, search:str):
	PEXELS_API_KEY = API_KEY['pexels']
	api = API(PEXELS_API_KEY)
	api.search(search, page=1, results_per_page=5)
	photos = api.get_entries()
	urls = []
	for photo in photos:
  	# Print photographer
		print('Photographer: ', photo.photographer)
  	# Print url
		print('Photo url: ', photo.url)
		urls.append(photo.original)
  	# Print original size url
		print('Photo original size: ', photo.original)
	await ctx.send(urls[0])

# get font-awesome 
@bot.command(name="fa")
async def font_awesome(ctx, *, search=""):
	result = read_as_dict("fa6/icons",search)
	faurl = read_as_dict("fa6/details", search)
	if "👻" in result:
		await ctx.send(format_text(result, "fix"))
		return

	await ctx.send(format_text(result, "html"))
	await btn_fa_detail(bot, ctx, faurl
	)

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


# Server info
@bot.command(name="info")
async def info_server(ctx):
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
	API_KEY["google"] = os.environ["KEY_GOOGLE"]
	API_KEY["pexels"] = os.environ["KEY_PEXELS"]
	bot.run(os.environ["DISCORD_TOKEN"])
