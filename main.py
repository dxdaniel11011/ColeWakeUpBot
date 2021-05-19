import discord, os

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$spamcole('):
    #   if message.content[11] in [1,2,3,4,5,6,7,8,9,0]:
    #       num = message.content[10:len(message.content)-1]
    #       for i in range(int(num)):
    #         await message.channel.send("q")
    #         await message.channel.send("<@145631773328539649> WAKE THE FUCK UP")
    #   else:
    for i in range(int(message.content[10:len(message.content)-1])):
      await message.channel.send("<@145631773328539649> WAKE THE FUCK UP")
      

TOKEN = os.getenv('TOKEN')
client.run(str(TOKEN))
