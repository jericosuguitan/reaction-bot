# Jerico Suguitan
# Python 3.8 using discord.py
# 12/18/2020

import discord
#from discord.ext import commands

token = "Nzg5NzAzMzU5NTE4MDgxMDM0.X916kA.wTz_b5lJf3z2P6pSuv65wTMVemQ"

intents = discord.Intents.all() 
# need intents to be true (in Discord applications website) to properly run
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is logged in.")

#@client.event
#async def on_message(self, message):
#    print ('on message event')
#    if message.author.bot:
#        return
#
#    if message.content.lower() == ('hi'):
#        await message.channel.send('hey!')
#
#    elif message.content.lower() == ('ping'):
#        await message.channel.send('pong!')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 789756930741633055:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'bloom':
            role = discord.utils.get(guild.roles, name='Bloom Fam')
        elif payload.emoji.name == 'hero':
            role = discord.utils.get(guild.roles, name='Hero Fam')
        elif payload.emoji.name == 'skybison':
            role = discord.utils.get(guild.roles, name='Sky Bison Fam')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            print(member)
            # testing: print(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print("added role")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 789756930741633055:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'bloom':
            role = discord.utils.get(guild.roles, name='Bloom Fam')
        elif payload.emoji.name == 'hero':
            role = discord.utils.get(guild.roles, name='Hero Fam')
            # testing: print("remove hero")
        elif payload.emoji.name == 'skybison':
            role = discord.utils.get(guild.roles, name='Sky Bison Fam')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members) 
            # need to use payload.user_id becauase on_raw_reaction_remove does not track member based on payload.member
            # testing: 
            print(member)
            if member is not None:
                await member.remove_roles(role)
                print("removed role")
            else:
                print("Member not found.")
        else:
            print("Role not found.")

client.run(token)