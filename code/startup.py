#This program shows how the on_ready event can be used to tell you when your bot is finished loading, or run any other functions

import discord

token = open("token.txt","r").read()
client = discord.Client()

@client.event
async def on_ready(self): #The on_ready event listens for when the bot starts and then prints to the console 'Bot online!'
    print('Bot online!')
    
client.run(token)
