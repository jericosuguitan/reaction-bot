import discord

token = ""


class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged in as " + str(self.user))

#    async def on_message(self, message):
#        if message.author.bot:
#            return
#
#        if message.content.lower() == ('hi'):
#            await message.channel.send('hey!')
#        
#        elif message.content.lower() == ('ping'):
#            await message.channel.send('pong!')

client = BotClient()
client.run(token)