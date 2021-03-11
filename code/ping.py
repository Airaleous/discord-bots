import discord

client = discord.Client() #Defines client

@client.event
async def on_message(ctx): #Waits for a message to be sent. 'ctx' is the message object
    if ctx.content == "ping!": #Checks message content for phrase
        await ctx.delete()
        await ctx.channel.send("Pong!") #Replies "Pong!" to the channel the message was sent in
    elif ctx.content == "notping!": #Checks message content for phrase
        await ctx.channel.send("NotPing!") #Replies "Pong!" to the channel the message was sent in


client.run('Your Token!') #Initializes the bot. Get your token from the Developer dashboard
