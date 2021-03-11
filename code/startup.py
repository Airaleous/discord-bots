import discord

token = open("token.txt","r").read()
client = discord.Client()

@client.event
async def on_ready(self): #The on_ready event listens for when the bot starts and then prints to the console 'Bot online!'
    print('Bot online!')
    
client.run(token)
