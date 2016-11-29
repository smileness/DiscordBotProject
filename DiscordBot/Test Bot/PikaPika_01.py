import datetime
import time
# import urllib.request
import urllib.parse

try:

    # time example
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # url = 'https://www.google.com/#q=apple'

    text = 'apple'
    url = 'https://www.youtube.com/results'
    values = {
        'search_query': text
    }

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data)

    resp = urllib.request.urlopen(req)

    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'}

    req = urllib.request.Request(url, headers=headers)

    resp = urllib.request.urlopen(req)

    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
    '''

    print(st)

except Exception as e:
    print(str(e))
