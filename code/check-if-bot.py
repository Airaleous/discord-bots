#Sometimes it's advantageous to ensure that your bot does not listen to other bots in a server.
#This can be done by checking if the author is a bot (Line 10) and returning (ending the statement) if they are.

import discord

token = open("token.txt","r").read()
client = discord.Client()

@client.event
async def on_message(ctx):
    if ctx.author.bot: #Checks if message author is a bot. Returns if True
        return
    if ctx.content == "ping!":
        await ctx.channel.send("Pong!")
        
client.run(token)
