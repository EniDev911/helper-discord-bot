import discord
import datetime

class Embed:
    def __init__(self, title, description,url=None, logo=None, color=0x1f6e9e):
        self.embed_title = title
        self.embed_description = description
        self.url = url
        self.embed_logo = logo
        self.embed_color = color
        self.timestamp = datetime.datetime.utcnow()
        self.embed = discord.Embed(title= self.embed_title, description= self.embed_description,timestamp= self.timestamp, color= self.embed_color)

    def create(self):
        self.embed.set_author(name=f"{self.description}", icon_url= self.embed_logo)
        self.embed.set_thumbnail(url="https://www.sciences-u-lyon.fr/images/2020/03/myges.png")
        self.embed.set_footer(text="Made by EniDev911")
        
    def add_field(self, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)

    def to_dict(self):
        return self.embed.to_dict()


embed_bootstrap = Embed('Bootstrap',
'source: getbootstrap.com/docs/5.2/utilities/text/',
'https://getbootstrap.com')

#embed_bootstrap.create()



	# embed.set_footer(text='This is a footer')
	# embed.set_image(url='https://badges.aleen42.com/src/codepen.svg')
	# embed.set_thumbnail(url='https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/96/000000/external-multi-platform-online-code-editor-and-open-source-learning-service-logo-shadow-tal-revivo.png')
	# embed.set_author(name='Codepen', icon_url='https://blog.codepen.io/wp-content/uploads/2012/06/Button-Fill-Black-Large.png')
	# embed.add_field(name='Field `localstorage`', value=file, inline=False)
	# embed.add_field(name='Field `localstorage`', value='```html\n<h1>HelloWorld</h1>\n```', inline=False)
	# embed.add_field(name='Field name', value='Field value', inline=True)
	# embed.add_field(name='Field name', value='Field value', inline=True)
