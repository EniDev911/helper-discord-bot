import os
from pydoc import doc
from .settings import PAPERS
from .formatter import format_text

# ===== read document and convert to dict
def read_as_dict(source:str,query:str, ext:str=".txt"):
	query = query.strip().replace(" ", "").lower()
	try:
		with open(os.path.join(PAPERS,source+ext)) as f:
			a = { k: v for line in f for (k, v) in [line.strip().split(None, 1)]}
		if query == "":
			file_clean = ""
			for k, v in a.items():
				file_clean += k+"\n"
			return file_clean
		
		return a[query]

	except FileNotFoundError as err:
		print(err)
		return f"No encontraré coincidencia de => '{query.upper()}' 👻"
	except KeyError as e:
		return f"No encontraré coincidencia de => '{query.upper()}' 👻"


# ===== read and clean document
def read(source: str, document: str, ext:str="txt",format:str="html"):
	doc = document.strip().replace(" ", "").lower()
	try:
		with open(os.path.join(PAPERS,source,doc+"."+ext) ,'r', encoding='utf-8') as file:
			file_clean = ""
			for readline in file:
				line_strip = readline.lstrip("\n")
				file_clean += line_strip
			return file_clean

	except FileNotFoundError as err:
		print(err)
		return format_text(f"No encontraré coincidencia de => '{document.upper()}' 👻", "fix")
