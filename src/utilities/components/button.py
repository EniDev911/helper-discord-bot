from ast import literal_eval
from ..settings import BASE_DIR
import discord
import discord_components
from discord_components import (
	Button,
	ButtonStyle,
	Select, 
	SelectOption
)
import asyncio
import pyperclip as pc
from ..formatter import format_text

blue = ButtonStyle.blue
green = ButtonStyle.green
# emojis : "📋"

async def btn_clipboard(bot, ctx, content=None):
	await ctx.send(
  	 components = [
			Button(style= blue, 
			emoji= "📋",
			label= "Copiar", 
			custom_id = "clipboard")]
			)
	interaction = await bot.wait_for(
		"button_click", check = lambda inter: inter.custom_id == "clipboard"
  		)
	if interaction is not None:
		await interaction.send(content = format_text("¡𝕮𝖔𝖕𝖎𝖆𝖉𝖔!👌", "fix"), ephemeral=False)
		return pc.copy(content)

async def btn_fa_detail(bot, ctx, faurl:str=""):
	cdn = '<script src="https://kit.fontawesome.com/6b8f0c7049.js" crossorigin="anonymous"></script>'
	btns = [Button(style=ButtonStyle.URL, 
			emoji= "🌐",
			url=faurl,
			label= "Detalles",
			custom_id = "url"
			), Button(style=green, 
			emoji= "🚀",
			label= "CDN",
			custom_id = "cdn"
			)]
	await ctx.send(components = [btns])
	interaction = await bot.wait_for(
		"button_click", check = lambda inter: inter.custom_id == "cdn"
  		)
	if interaction is not None:
		await interaction.send(content = format_text(cdn, "html"), ephemeral=False)


async def btn_github(bot, ctx, content=None):
	await ctx.send(
  	 components = [
			Button(style= blue, 
			emoji= "🥷🏻", 
			label= "Copiar", 
			custom_id = "github")]
			)
	interaction = await bot.wait_for(
		"button_click", check = lambda inter: inter.custom_id == "clipboard"
  		)
	if interaction is not None:
		await interaction.send(content = format_text("¡𝕮𝖔𝖕𝖎𝖆𝖉𝖔!👌", "fix"), ephemeral=False)
		return pc.copy(content)