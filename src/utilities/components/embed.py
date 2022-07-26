import discord
import datetime
from ..url import LOGO

class Embed:
    def __init__(self, title: str, description: str,url=None, color=0x1f6e9e):
        self.embed_title = title
        self.embed_description = description
        self.url = url
        self.embed_color = color
        self.timestamp = datetime.datetime.utcnow()
        self.embed = discord.Embed(title= self.embed_title, 
                                    description= self.embed_description,
                                    timestamp= self.timestamp, 
                                    color= self.embed_color)
    def create(self, name, logo):
        self.embed.set_author(name=name, icon_url=logo)
        self.embed.set_thumbnail(url=logo)
        self.embed.set_footer(text=name)
        
    def add_field(self, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed.to_dict()



def info(ctx):
    emb_info =  Embed(
    title = f"{ctx.guild.name}",
    description = "Servidor para ayudar y jugar")
    emb_info.create(f"{ctx.guild.owner}", f"{ctx.guild.icon_url}")
    emb_info.add_field("Servidor creado el:", f"{ctx.guild.created_at.strftime('%Y-%m-%d')}")
    emb_info.add_field("Servidor Región:", f"{ctx.guild.region}")
    emb_info.add_field("Servidor ID:", f"{ctx.guild.id}")
    return emb_info

def error(ctx, message):
    emb_error = Embed(
        title = f"{ctx.guild.name}",
        description = f"{message}")
    return emb_error


embed_bootstrap = Embed(
    title = 'Bootstrap', 
    description = 'source: getbootstrap.com/docs/5.2/utilities/text/',
    url = 'https://raw.githubusercontent.com/EniDev911/assets/main/galery/svg/logos/bootstrap-5.svg')
embed_bootstrap.create("bootstrap", "bootstrap-5.png")
embed_bootstrap.add_field("example", "Test value", False)
