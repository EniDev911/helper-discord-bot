#---------------------------------------#
#        Module: main					|
#        Author: Marco Contreras		|
#         Email: enidev911@gmail.com 	|
# 										|
#     Copyright: (c) EniDev911			|
#       Licence: GPL 3.0 				|
#---------------------------------------#

import discord
from discord.ext import commands
import os
import datetime 
from urllib import parse, request
import re

bot = commands.Bot(command_prefix=">", description="Este es un bot creado por EniDev911")

# ===== read documents
def read(document: str):
	dirname = os.path.dirname(__file__)
	with open(os.path.join(dirname+'/papers', document) ,'r', encoding='utf-8') as file:
		f = file.read()
		return f

# ==== show examples
@bot.command()
async def ejemplo(ctx, *, search: str):
	result = search.strip()
	try:
		file = read('js/'+result+'.md')
		await ctx.send(file)
	except FileNotFoundError as err:
		await ctx.send("**No encontre coincidencia**") 

# ===== youtube get popular video
@bot.command()
async def yt(ctx, *, search):
	query_string = parse.urlencode({'search_query': search})
	html_content = request.urlopen("http://www.youtube.com/results?"+query_string)
	results = re.findall('\"\\/watch\\?v=(.{11})', html_content.read().decode())
	#print(results)
	await ctx.send('https://youtube.com/watch?v='+results[0])

# ===== js get mdn reference
# @bot.command()
# async def js(ctx, *, search):
# 	query_string = parse.urlencode({'search_query': search})
# 	embed = discord.Embed(
# 		title = 'Title',
# 		description = 'This is a description',
# 		timestamp=datetime.datetime.utcnow(),
# 		color=0xf9f06b
# 		)
# 	embed.set_footer(text='This is a footer')
# 	embed.set_image(url='https://raw.githubusercontent.com/EniDev911/enidev911_guides/main/assets/png/prompt.png')
# 	embed.set_thumbnail(url='https://raw.githubusercontent.com/EniDev911/enidev911_guides/main/assets/png/prompt.png')
# 	embed.set_author(name='EniDev911', icon_url='https://avatars.githubusercontent.com/u/70834807?v=4')
# 	embed.add_field(name='Field name', value='Field value', inline=False)
# 	embed.add_field(name='Field name', value='Field value', inline=True)
# 	embed.add_field(name='Field name', value='Field value', inline=True)

# 	await ctx.send(embed=embed)


@bot.command()
async def help_(ctx):
	await ctx.send('Lista un comando para ver ejemplo'+\
		           '- pwd\n' +\
		           '- echo\n');


@bot.command()
async def ls(ctx):
	file = read('ls_command.md')
	await ctx.send(file);


@bot.command()
async def echo(ctx):
	await ctx.send("Sirve para imprimir por la salida estándar una expresión:" +\
				   "```bash\n"+\
				   "echo 'Soy LUNA'"+\
				   "```");


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

# require token 
bot.run(os.environ["DISCORD_TOKEN"])

