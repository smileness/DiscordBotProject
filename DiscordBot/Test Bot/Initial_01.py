import discord
import time
import datetime
import discordToken
import urllib.request
import re

"""Just some little python3 discord project"""

__author__ = "NA Xu"
__copyright__ = "Copyright 2016"

try:
    client = discord.Client()


    def example_func(author, message):
        client.send_message(message.channel, "%s, How are you doing?" % author)


    def is_me(m):
        return m.author == client.user


    def youtube_search(message):
        if len(message.content.split()) == 1:
            pass
        else:
            text_to_search = message.content.replace('!youtube ', '')
            query = urllib.request.quote(text_to_search)
            url = 'https://www.youtube.com/results?search_query=' + query
            return url


    def youtube_name(message):
        text_name = message.content.replace('!youtube -w ', '')
        return text_name


    def youtube_results(file_name):
        if file_name == '':
            pass
        else:
            print(file_name)

            url = 'http://www.youtube.com/results?'

            # search_name = urllib.request.quote(file_name)

            parse_value = dict()
            parse_value['search_query'] = file_name

            data = urllib.parse.urlencode(parse_value)
            # data = data.encode('utf-8')
            # req = urllib.request.Request(url, data)

            req = url + data

            resp = urllib.request.urlopen(req)

            resp_data = resp.read()

            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', resp_data.decode())

            return search_results[0]


    def google_search(message):
        if len(message.content.split()) == 1:
            pass
        else:
            text_to_search = message.content.replace('!google ', '')
            query = urllib.request.quote(text_to_search)
            url = 'https://www.google.com/#q=' + query
            return url


    @client.event
    async def on_message(message):
        # debug
        whoami = client.user
        print(whoami)

        # Avoid bot reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!time'):
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            msg = 'It is : %s' % (st)
            await client.send_message(message.channel, msg)

        if message.content.startswith('$start'):
            await client.send_message(message.channel, 'Type $stop 4 times.')
            for i in range(4):
                # For particular end user count
                # await client.wait_for_message(author=message.author, content='$stop')

                await client.wait_for_message(content='$stop')
                fmt = '{} left to go...'
                await client.send_message(message.channel, fmt.format(3 - i))
            await client.send_message(message.channel, 'Good job!')

        if message.content.startswith('$cool'):
            await client.send_message(message.channel, 'Who is cool in this channel? Type $name here')

            def check(x):
                return x.content.startswith('$name')

            # For particular end user count
            # message = await client.wait_for_message(author=message.author, check=check)
            message = await client.wait_for_message(check=check)
            # name = message.content[len('$name'):].strip()
            await client.send_message(message.channel, '{0.author.mention} is cool indeed'.format(message))

        if message.content.startswith('!yell'):
            await client.send_message(message.channel, 'Hey Sweety!', tts=True)

        if message.content.startswith('!youtube') & ('-w' not in message.content):
            msg = youtube_search(message)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!youtube') & ('-w' in message.content):
            search_name = youtube_name(message)

            # Only get first element form results set
            play_index = youtube_results(search_name)

            url = 'http://www.youtube.com/watch?v=' + urllib.request.quote(play_index)
            await client.send_message(message.channel, url)

        if message.content.startswith('!google'):
            msg = google_search(message)
            await client.send_message(message.channel, msg)


    @client.event
    async def on_ready():
        print('------------')
        print('Logged in as')
        print('------------')
        print(client.user.name)
        print(client.user.id)
        print('------------')


    token = discordToken.token()
    client.run(token)

except Exception as e:
    print(str(e))
