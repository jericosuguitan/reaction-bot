# from dotenv import load_dotenv
# load_dotenv()

import asyncio

import os
BOT_TOKEN = os.getenv('BOT_TOKEN')

import discord
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

# @client.event
# async def on_client_error():
#     await client.on_error("error")

@client.event
async def on_ready():
        # await client.login(BOT_TOKEN)
        print("Bot is logged in.")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 789756930741633055:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        
        # allFams = [discord.utils.get(guild.roles, name='Bloom Fam'), discord.utils.get(guild.roles, name='Hero Fam'), discord.utils.get(guild.roles, name='Sky Bison Fam')]
        # member = payload.member
        # famCheck = any(item in member.roles for item in allFams)
        # # if member already has one of three fam roles 
        # if famCheck:
            
        # else: # not true, aka no fam

        # allFams = [discord.utils.get(guild.roles, name='Bloom Fam'), discord.utils.get(guild.roles, name='Hero Fam'), discord.utils.get(guild.roles, name='Sky Bison Fam')]
        # member = payload.member
        # haveFam = any(item in member.roles for item in allFams)

        # if payload.emoji.name == 'bloom':
        #     role = discord.utils.get(guild.roles, name='Bloom Fam')
        # elif payload.emoji.name == 'hero':
        #     role = discord.utils.get(guild.roles, name='Hero Fam')
        # elif payload.emoji.name == 'skybison':
        #     role = discord.utils.get(guild.roles, name='Sky Bison Fam')
        # else:
        #     role = discord.utils.get(guild.roles, name= payload.emoji.name)

        allFams = [discord.utils.get(guild.roles, name='Hero Fam'), discord.utils.get(guild.roles, name='Brace Fam')]
        member = payload.member
        haveFam = any(item in member.roles for item in allFams)

        if payload.emoji.name == 'hero2':
            role = discord.utils.get(guild.roles, name='Hero Fam')
        elif payload.emoji.name == 'brace':
            role = discord.utils.get(guild.roles, name='Brace Fam')
        else:
            role = discord.utils.get(guild.roles, name= payload.emoji.name)
            
        if haveFam & (role in allFams):
            print("should not assign role")
            return
        
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

        # if payload.emoji.name == 'bloom':
        #     role = discord.utils.get(guild.roles, name='Bloom Fam')
        # elif payload.emoji.name == 'hero':
        #     role = discord.utils.get(guild.roles, name='Hero Fam')
        #     # testing: print("remove hero")
        # elif payload.emoji.name == 'skybison':
        #     role = discord.utils.get(guild.roles, name='Sky Bison Fam')
        # else:
        #     role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if payload.emoji.name == 'hero2':
            role = discord.utils.get(guild.roles, name='Hero Fam')
        elif payload.emoji.name == 'brace':
            role = discord.utils.get(guild.roles, name='Brace Fam')
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

# idea by anna : HERO FAM - daily positive affirmations

client.run(BOT_TOKEN)