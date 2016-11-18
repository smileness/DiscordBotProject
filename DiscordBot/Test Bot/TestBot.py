import discord
# import password_omg

# This is the code for disable SSL warning nothing very import!
import requests.packages.urllib3

# requests.packages.urllib3.disable_warnings()

client = discord.Client()


def example_func(author, message):
    client.send_message(message.channel, "%s, How are you doing?" % author)


@client.event
def on_message(message):
    author = message.author
    if message.content.startswith('!test'):
        example_func(author, message)


password = '3191208aXuq'  # password_omg.my_password()
client.run('olinayas@gmail.com', password)

client.accept_invite('https://discord.gg/kEX98')

client.close()
