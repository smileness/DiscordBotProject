import discord
import time
import datetime

client = discord.Client()


def example_func(author, message):
    client.send_message(message.channel, "%s, How are you doing?" % author)


# Main bot body
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
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


# This is for login information
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('MjQ5MDkyMDEzNDQwNDk5NzEy.CxBSVA.11-GDXTPkko6EQ4zPNMU6vGPF5U')
