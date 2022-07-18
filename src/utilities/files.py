import os
from .settings import PAPERS
import zipfile     

# ===== read and clean document
def read(document: str):

	with open(os.path.join(PAPERS, document) ,'r', encoding='utf-8') as file:
		file_clean = ""
		for readline in file:
			line_strip = readline.lstrip("\n")
			file_clean += line_strip
		return file_clean