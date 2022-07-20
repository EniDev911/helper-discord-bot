import os
from pydoc import doc
from .settings import PAPERS
import zipfile     

# ===== read and clean document
def read(document: str):
	doc = document.strip().replace(" ", "").lower()
	ext = ".md"
	try:
		with open(os.path.join(PAPERS, doc+ext) ,'r', encoding='utf-8') as file:
			file_clean = ""
			for readline in file:
				line_strip = readline.lstrip("\n")
				file_clean += line_strip
			return file_clean

	except FileNotFoundError as err:
		print(err)
		return "**No encontre coincidencia**"