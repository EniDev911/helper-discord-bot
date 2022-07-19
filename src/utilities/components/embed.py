import discord
import datetime
from ..url import logo

class Embed:
    def __init__(self, title: str, description: str,url=None, logo=None, color=0x1f6e9e):
        self.embed_title = title
        self.embed_description = description
        self.url = url
        self.embed_logo = logo
        self.embed_color = color
        self.timestamp = datetime.datetime.utcnow()
        self.embed = discord.Embed(title= self.embed_title, 
                                    description= self.embed_description,
                                    timestamp= self.timestamp, 
                                    color= self.embed_color)
    def create(self, name, icon):
        self.embed.set_author(name=name, icon_url= logo+icon)
        self.embed.set_thumbnail(url=logo+icon)
        self.embed.set_footer(text=name)

        
    def add_field(self, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed.to_dict()


embed_bootstrap = Embed(
    title = 'Bootstrap', 
    description = 'source: getbootstrap.com/docs/5.2/utilities/text/',
    url = 'https://raw.githubusercontent.com/EniDev911/assets/main/galery/svg/logos/bootstrap-5.svg')
embed_bootstrap.create("bootstrap", "bootstrap-5.png")
embed_bootstrap.add_field("example", "Test value", False)

# This is the user input
# user_input = {'field name': 'some name', 'field value': 'some value'}

# # Getting the embed and converting it to a dict
# embed = message.embeds[0]
# embed_dict = embed.to_dict()

# for field in embed_dict['fields']:
#     if field['name'] == user_input['field name']:
#         field['value'] = user_input['field value']

# # Converting the embed to a `discord.Embed` obj
# edited_embed = discord.Embed.from_dict(embed_dict)

# # Editing the message
# await message.edit(embed=edited_embed)

# embed.set_footer(text='This is a footer')
# embed.set_image(url='https://badges.aleen42.com/src/codepen.svg')
# embed.set_thumbnail(url='https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/96/000000/external-multi-platform-online-code-editor-and-open-source-learning-service-logo-shadow-tal-revivo.png')
# embed.set_author(name='Codepen', icon_url='https://blog.codepen.io/wp-content/uploads/2012/06/Button-Fill-Black-Large.png')
# embed.add_field(name='Field `localstorage`', value=file, inline=False)
# embed.add_field(name='Field `localstorage`', value='```html\n<h1>HelloWorld</h1>\n```', inline=False)
# embed.add_field(name='Field name', value='Field value', inline=True)
# embed.add_field(name='Field name', value='Field value', inline=True)
