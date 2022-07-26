from urllib import error, request

url = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"

try:
  url_data = request.urlopen(url)
  print(url_data)
  for line in url_data:
    print(line.decode('utf-8').strip())
except error as err:
  print("Error: ", err)