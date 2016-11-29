import discord
import time
import datetime
import discordToken
import urllib.request

import re

str = '!youtube -w apple juice'
data = str.replace('!youtube -w', '')

print(data)

query_string = urllib.parse.urlencode({"search_query": input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print(search_results[0])
print("http://www.youtube.com/watch?v=" + search_results[0])
