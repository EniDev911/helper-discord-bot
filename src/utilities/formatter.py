def format_text(text:str, format:str=None, bold:bool=False, italic:bool=False):
	if bold and italic:
		return f"**_{text}_**"

	elif italic:
		return f"_{text}_"

	elif bold:
		return f"**{text}**"

	return f"```{format}\n{text}```"

def format_url(url:str="", rule:str="", format:str=None):
	body = "body {"+"\n"+"\tfont-family: "+"{}".format(rule)+"\n"+"}"
	if format == "css":
		return f"@import url('{url}');\n{body}"
	elif format == "html":
		return f"<link href='{url}' rel='stylesheet'>"

#https://fonts.googleapis.com/css2?
# family=Ubuntu+Mono:wght@400;700&display=swap
# def format_fonts(family=str="", wght=[], format:str=""):
# 	if format == "css":
# 		return f"@import url('https://fonts.googleapis.com/css2?family={family}');\n{body}"
# 	elif format == "html":
# 		return f"<link href='{url}' rel='stylesheet'>"
