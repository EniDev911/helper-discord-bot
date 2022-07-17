### discord.on_ready()

Se llama cuando el **cliente** termina de preparar los datos recibidos de Discord. Por lo general, después de que el inicio de sesión sea exitoso y el Client.guilds co. se llenan

```py
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Un comando"))
	print("My boot is Ready")
```