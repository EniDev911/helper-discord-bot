import re
from urllib import parse, request
import json
from .settings import API_KEY
from .url import googleFonts
from googlesearch import search


# youtube get popular video
def youtube_search(query):
	query_string = parse.urlencode({'search_query': query})
	html_content = request.urlopen("http://www.youtube.com/results?"+query_string)
	results = re.findall('\"\\/watch\\?v=(.{11})', html_content.read().decode())
	return 'https://youtube.com/watch?v='+results[0]


# get google results
def google_search(query):
	return list(search(query, start=0, stop=1, lang="es"))[0]
	

# def get_google_fonts(family: str =""):
# 	popularity = parse.urlencode({'sort':'popularity'})
# 	family = family.capitalize()
# 	try:
# 		response = request.urlopen(googleFonts+API_KEY['google']+'&'+popularity)
# 		print(googleFonts+API_KEY['google']+'&'+popularity)
# 		if (response.getcode()==200):
# 			data = response.read()
# 			dataJson = json.loads(data)
# 			#return [dataJson["items"][0]]
# 			families = []
# 			for i in range(50):
# 				#if(family == i["family"]):
# 				#	print(i["variants"])
# 				#	return i["variants"]
# 				#print(f'{i["family"]} {i["variants"]}')
# 				families.append(dataJson["items"][i]["family"])
# 			return "\n".join(families) 
# 	except Exception as e:
# 		print(e, "Error occured", response.getcode())

