from ..setting import BASE_DIR

print(BASE_DIR)


# @bot.command(pass_context=True)
# async def button(ctx):
# 	await ctx.send(
# 		"ABRIR EN CODEPEN",
# 		components = [

# 			Button(style= ButtonStyle.black, emoji="🧑🏽‍💻", label="ABRIR EN CODEPEN",
# 			custom_id = "button1")
# 		])

# 	interaction = await bot.wait_for(
# 		"button_click", check = lambda inter: inter.custom_id == "button1"
# 		)
# 	google = webbrowser.open("https://codepen.io/EniDev911/pen/jOzVzeK ")
# 	await interaction.send(content = google, ephemeral=False)
# 	


# @bot.command()
# async def select(ctx):
#     await ctx.send(
#         "Selects!",
#         components=[
#             Select(
#                 placeholder="Select something!",
#                 options=[
#                     SelectOption(label="a", value="a"),
#                     SelectOption(label="b", value="b"),
#                 ],
#                 custom_id="select1",
#             )
#         ],
#     )