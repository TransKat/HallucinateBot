import discord
from discord.ext import commands
import random

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #@commands.command(brief="Kicks a user from the current server.")
    #@commands.has_permissions(kick_members=True)
    #async def kick(ctx, user: discord.Member, *, reason=None):
        #await user.kick(reason=reason)
        #await ctx.send(f"{user} have been kicked sucessfully")
        #await ctx.message.add_reaction("✅")    

    @commands.command(brief="Bans someone")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user:discord.Member, *, reason=None):
        """Casts users out of heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f"{user.mention} was cast out of the server for {reason}.")
            await ctx.message.add_reaction("✅")
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot")
    
    @commands.command(brief="Kicks someone from the server")
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, user:discord.Member, *, reason=None):
        """Casts users out of heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.kick(user, reason=reason)
            await ctx.send(f"{user.mention} was cast out of the server for {reason}.")
            await ctx.message.add_reaction("✅")
        except discord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot")
    

    @commands.command(brief="Purges x amount of messages.")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, arg):
        await ctx.channel.purge(limit=int(arg)+1)
        await ctx.send(f"Purged {arg} messages")
        await ctx.message.add_reaction("✅")

    @commands.command(brief="Creates a channel with a specified name")
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, name=None, *, description=None):
        await ctx.guild.create_text_channel(name, topic=description)
        await ctx.send(f"Channel {name} created")



def setup(bot):
    bot.add_cog(moderation(bot))
