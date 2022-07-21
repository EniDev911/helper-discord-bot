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


# @bot.command()
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
