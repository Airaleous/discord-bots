#This is a simple program that waits for a message event (Line 8), checks the content of the message (Line 9), and responds to the message (Line 10)

import discord

client = discord.Client() #Defines client

@client.event
async def on_message(ctx): #Waits for a message to be sent. 'ctx' is the message object
    if ctx.content == "ping!": #Checks message content for phrase
        await ctx.channel.send("Pong!") #Replies "Pong!" to the channel the message was sent in

client.run('Your Token!') #Initializes the bot. Get your token from the Developer dashboard
