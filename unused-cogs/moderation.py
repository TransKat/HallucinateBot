import discord
from discord.ext import commands
import random

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(brief="Kicks a user from the current server.")
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        await ctx.send(f"{user} have been kicked sucessfully")
        await ctx.message.add_reaction("✅")    

    @commands.command(brief="Bans the mentioned memeber from the current server.")
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        await ctx.send(f"{user} have been bannned sucessfully")
        await ctx.message.add_reaction("✅")
    
    @commands.command(brief="Unbans a user.")
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
  
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user} have been unbanned sucessfully")
            return
            await ctx.message.add_reaction("✅")

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