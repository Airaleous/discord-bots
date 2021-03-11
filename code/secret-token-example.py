import discord

token = open("token.txt","r").read() #Tokens are secret. Opens the token text file and stores it in the token variable
client = discord.Client() #Defines client

@client.event
async def on_message(ctx): #Waits for a message to be sent. 'ctx' is the message object
    if ctx.content == "ping!": #Checks message content for phrase
        await ctx.channel.send("Pong!") #Replies "Pong!" to the channel the message was sent in

client.run(token) #Initializes the bot
