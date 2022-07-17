import re
from urllib import parse, request

# youtube get popular video
def youtube(search):
	query_string = parse.urlencode({'search_query': search})
	html_content = request.urlopen("http://www.youtube.com/results?"+query_string)
	results = re.findall('\"\\/watch\\?v=(.{11})', html_content.read().decode())
	#print(results)
	return 'https://youtube.com/watch?v='+results[0]




# get fonts google api
def google_font(font):
	if font.lower() == "roboto":
		return "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap"
