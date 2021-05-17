## Hallucinate - 21.05


import discord
import os
import time
import json
import random
from discord.ext import commands

version = "Hallucinate 21.05 - Resurgance - h! or h."

# loads the token from token.txt

with open('./token.txt') as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix = ["h!","h.","h$",")"],case_insensitive=True)

@client.event
async def on_ready():
    print('Bot is online.')
    activity = discord.Game(name=f"{version}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    return

#discord.py error handler
@client.event
async def on_command_error(ctx, error):
    await ctx.reply(error)
    print(f"Error caused by {ctx.author}. {error}")
    await ctx.message.add_reaction("❌")

@client.command()
@commands.is_owner()
async def setversion(ctx, * , arg,):
    global version
    version = arg
    await ctx.send(f"The version has been set to {arg}")
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.message.add_reaction("✅")

@client.command()
@commands.is_owner()
async def setstatus(ctx, *, arg):
    activity = discord.Game(name=f"{arg}", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send(f"You changed the bot's status to: Playing **{arg}**")
    await ctx.message.add_reaction("✅")

@client.command()
@commands.is_owner()
async def leave(ctx):
    await ctx.send(f"The bot is now leaving {ctx.guild.name}")
    await ctx.guild.leave()
    await ctx.message.add_reaction("✅")

@client.command()
async def about(ctx):
    embed = discord.Embed(
        title = 'About Hallucinate',
        description = "Hallucinate was originally released in late 2020, as a moderation bot.\nBut, now, in it's current state it focuses both on moderation and fun.",
        colour = discord.Colour.green()

    )
    await ctx.send(embed=embed)

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
    await ctx.message.add_reaction("✅")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog {extension} unloaded")
    await ctx.message.add_reaction("✅")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Cog {extension} has been reloaded.")
    await ctx.message.add_reaction("✅")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
@commands.is_owner()
async def guilds(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()
    await ctx.send(f"{client.guilds}\n")

@client.command()
@commands.is_owner()
async def eval(ctx, *, arg):
    exec(arg)
    await ctx.message.add_reaction("✅")

@client.command()
@commands.is_owner()
async def get_resource(ctx, arg):
    if arg == "token.txt":
        await ctx.send("You've been denied access to this file.")
        await ctx.message.add_reaction("❌")
    else:    
        await ctx.channel.send(file=discord.File(arg))
        print(f"Successfully gathered and uploaded {arg}.")
        await ctx.message.add_reaction("✅")

client.run(TOKEN)
