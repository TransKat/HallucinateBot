import discord
import os
import json
import random
from discord.ext import commands

version = "Release 2 - The Revival"

# loads the token from token.txt

with open('./token.txt') as f:
    TOKEN = f.read()

# gets the server prefix and stores it in a variable

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = "h!",case_insensitive=True)

@client.event
async def on_ready():
    print('Bot is online.')
    activity = discord.Game(name=f"{version}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    return

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)]  = 'h!'  

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)




    print(f"Joined {guild} ID: {guild.id}")


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)


#The below code bans player.


@client.command()
@commands.is_owner()
async def setversion(ctx, * , arg,):
    global version
    version = arg
    await ctx.send(f"The version has been set to {arg}")
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.command()
@commands.is_owner()
async def setstatus(ctx, *, arg):
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send(f"You changed the bot's status to: Playing **{arg}**")

@client.command()
@commands.is_owner()
async def leave(ctx):
    await ctx.send(f"The bot is now leaving {ctx.guild.name}")
    await ctx.guild.leave()

@client.command()
@commands.is_owner()
async def ownersay(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} loaded")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} unloaded")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been reloaded.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


## changes prefix. deprecated feature.

##@client.command(name="Prefix",brief="Changes the server prefix",hidden=True)
##@commands.has_permissions(ban_members = True)
##async def changeprefix(ctx, prefix): 
    ##with open('prefixes.json', 'r') as f:
        ##prefixes = json.load(f)

    ##prefixes[str(ctx.guild.id)] = prefix  

    ##with open('prefixes.json', 'w') as f:
        ##json.dump(prefixes, f, indent = 4)
    ##await ctx.send(f"Changed the server prefix to {prefix}")

@client.command()
@commands.is_owner()
async def guilds(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()
    await ctx.send(f"{client.guilds}\n")

client.run(TOKEN)