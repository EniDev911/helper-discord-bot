def format_text(text:str, format:str=None, bold:bool=False, italic:bool=False):
	if bold and italic:
		return f"**_{text}_**"

	elif italic:
		return f"_{text}_"

	elif bold:
		return f"**{text}**"

	return f"```{format}\n{text}```"