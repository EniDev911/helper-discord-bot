import re
from urllib import parse, request
from googlesearch import search

# youtube get popular video
def youtube_search(query):
	query_string = parse.urlencode({'search_query': query})
	html_content = request.urlopen("http://www.youtube.com/results?"+query_string)
	results = re.findall('\"\\/watch\\?v=(.{11})', html_content.read().decode())
	return 'https://youtube.com/watch?v='+results[0]


# get google results
def google_search(query):
	return list(search(query, start=0, stop=1, lang="es"))
	
