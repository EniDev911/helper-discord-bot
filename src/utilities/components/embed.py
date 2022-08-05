import discord
import datetime
from ..url import LOGO, pbAnimate, pbAnimateBack
import pokebase as pb
from googletrans import Translator  


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
    def create(self, name:str="", avatar:str="",thumbnail:str="", image:str=""):
        self.embed.set_author(name=name, icon_url=avatar)
        self.embed.set_thumbnail(url=thumbnail)
        self.embed.set_image(url=image)
        self.embed.set_footer(text=name)
        
    def add_field(self, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed.to_dict()



def info(ctx):
    emb_info =  Embed(
    title = f"{ctx.guild.name}",
    description = f"{ctx.guild.description}")
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

def pokemon(ctx, pkm):
    translator = Translator()  

    # 1: rojo, 2: verde
    colores = [0xfb1d04, 0x36f26e, 0xa12680, 0xffd375]
    color = 0xfb1d04
    ext = '.gif'
    pokemon = pb.pokemon(pkm.lower())
    abilities = ""
    types = ""
    description = ""
    for ability in pokemon.abilities:
        abilities += ability.ability.names[5].name+', '
        description += ability.ability.effect_entries[1].short_effect

    description = translator.translate(description, dest="es")

    for poketype in pokemon.types:
        if poketype.type.names[5].name.lower() == 'agua':
            types += '🌊 '+poketype.type.names[5].name
        elif poketype.type.names[5].name.lower() == 'dragón':
            types += '🐲 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'eléctrico':
            types += '⚡ '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'fuego':
            types += '🔥 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'hielo':
            types += '❄️ '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'roca':
            types += '🪨 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'normal':
            types += '✨ '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'acero':
            types += '🧲 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'tierra':
            types += '🟤 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'planta':
            types += '🌱 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'psíquico':
            types += '🌀 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'veneno':
            types += '🟣 '+poketype.type.names[5].name+' '
        elif poketype.type.names[5].name.lower() == 'lucha':
            types += '🥊 '+poketype.type.names[5].name+' '

    if 'agua' in types.lower():
        color = 0x1e8df6
    elif 'dragón' in types.lower():
        color = 0x7553ee
    elif 'eléctrico' in types.lower():
        color = 0xf2eb07
    elif 'fuego' in types.lower():
        color = 0xfb1d04
    elif 'hielo' in types.lower():
        color = 0x7dcbf2
    elif 'veneno' in types.lower():
        color = 0xa12680
    elif 'roca' in types.lower():
        color = 0xbababa
    elif 'tierra' in types.lower():
        color = 0xffd375
    elif 'normal' in types.lower():
        color = 0xffffff
    elif 'lucha' in types.lower():
        color = 0x885959
    elif 'planta' in types.lower():
        color = 0x36f26e
    elif 'psíquico' in types.lower():
        color = 0xdf77d6
    elif 'bicho' in types.lower():
        color = 0x5b9603

    emb_pokemon =  Embed(
    title = f"{pkm.capitalize()}",
    description = f"{description.text}",
    color=color)
    emb_pokemon.create(thumbnail=f"{pbAnimate+str(pokemon.id)+ext}", image=f"{pbAnimateBack+str(pokemon.id)+ext}")
    emb_pokemon.add_field("Altura:", f"{pokemon.height}")
    emb_pokemon.add_field("Peso:", f"{pokemon.weight}")
    emb_pokemon.add_field("Tipo:", f"{types}", False)
    emb_pokemon.add_field("Habilidades:", f"{abilities[0:-2]}", False)
    return emb_pokemon


# embed_bootstrap = Embed(
#     title = 'Bootstrap', 
#     description = 'source: getbootstrap.com/docs/5.2/utilities/text/',
#     url = 'https://raw.githubusercontent.com/EniDev911/assets/main/galery/svg/logos/bootstrap-5.svg')
# embed_bootstrap.create("bootstrap", "bootstrap-5.png")
# embed_bootstrap.add_field("example", "Test value", False)
