#---------------------------------------
#        Module: main										
#        Author: Marco Contreras		
#         Email: enidev911@gmail.com 	
# 										
#     Copyright: (c) EniDev911			
#       Licence: GPL 3.0 				
#---------------------------------------

from dis import disco
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

# intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", description="Este es un bot creado por EniDev911")

DiscordComponents(bot)

# GLOBAL
BASE_DIR = os.path.dirname(__file__)



@bot.command()
async def playlist(ctx):
	channel = discord.utils.get(ctx.guild.channels, name="hydra-song-requests")
	#channel = bot.get_channel(int(channel.id))
	#await channel.send("pokemon")
	
	await bot.get_channel(int(channel.id)).send("play pokemon", file=discord.File(os.path.join(BASE_DIR,"img")+"/logo_con_bg.png"))
	# print(os.path.join(BASE_DIR, "img")+"/logo_con_bg.png")
	await ctx.send(ctx.guild.name)
	

@bot.command(pass_context=True)
async def button(ctx):
	await ctx.send(
		"ABRIR EN CODEPEN",
		components = [

			Button(style= ButtonStyle.black, emoji="🧑🏽‍💻", label="ABRIR EN CODEPEN",
			custom_id = "button1")
		])

	interaction = await bot.wait_for(
		"button_click", check = lambda inter: inter.custom_id == "button1"
		)
	google = webbrowser.open("http://www.github.com/EniDev911")
	await interaction.send(content = google, ephemeral=False)
	

@bot.command()
async def select(ctx):
    await ctx.send(
        "Selects!",
        components=[
            Select(
                placeholder="Select something!",
                options=[
                    SelectOption(label="a", value="a"),
                    SelectOption(label="b", value="b"),
                ],
                custom_id="select1",
            )
        ],
    )


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
		await ctx.send(
		"ABRIR EN CODEPEN",
		components = [

			Button(style= ButtonStyle.blue, emoji="🧑🏽‍💻", label="ABRIR EN CODEPEN",
			custom_id = "button1")
		])

		interaction = await bot.wait_for(
		"button_click", check = lambda inter: inter.custom_id == "button1"
		)
		
		await interaction.send(content = webbrowser.open(f"http://www.github.com/EniDev911"), ephemeral=True)
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
				   "```")


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
	bot.run(os.environ["DISCORD_TOKEN"])

