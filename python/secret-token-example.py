#Your bot token is how you control your bot. It's important that no one discover your bot token (It can be rest in the developer dashboard).
#A good way to avoid leaking your token is loading it from an external file (Line 6) and storing it a token variable.
#From there, the token variable can be used in place of your actual token in your code

import discord

token = open("token.txt","r").read() #Tokens are secret. Opens the token text file and stores it in the token variable
client = discord.Client() #Defines client

@client.event
async def on_message(ctx): #Waits for a message to be sent. 'ctx' is the message object
    if ctx.content == "ping!": #Checks message content for phrase
        await ctx.channel.send("Pong!") #Replies "Pong!" to the channel the message was sent in

client.run(token) #Initializes the bot
