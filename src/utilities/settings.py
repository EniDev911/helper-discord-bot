import discord
import os
import os.path as path

## GlOBAL 
BASE_DIR = path.abspath(os.getcwd())
PAPERS = path.join(BASE_DIR, 'src', 'papers')
#BASE_DIR = path.dirname(__file__)

DISCORD = {
	"version" : discord.version_info
}



