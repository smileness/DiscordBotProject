import urllib.request
import urllib.parse
import json
import scrapy

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.5&"

search_name = input("What do you want to search for ? >> ")

parse_value = dict()

parse_value['q'] = search_name

query = urllib.parse.urlencode(parse_value)

url = url + query

response = urllib.request.urlopen(url).read()

print(response)

data = json.loads(response)

results = data['responseData']['results']

for result in results:
    title = result['title']
    url = result['url']
    print(title + '; ' + url)
