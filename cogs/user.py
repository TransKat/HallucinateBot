import discord
import time
import datetime
from discord.ext import commands
import random

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(brief="Says hello")
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command(brief="Info about the current server.")
    async def serverinfo(self, ctx):
        icon = ctx.guild.icon_url
        content = f"Name: {ctx.guild.name}\nID: {ctx.guild.id}\nOwner: <@{ctx.guild.owner_id}>\nBoosts: {ctx.guild.premium_subscription_count}\nCreated: {ctx.guild.created_at}"
        embed = discord.Embed(
            title = ctx.guild.name,
            description = content,
            colour = discord.Colour.green()


        )
        embed.set_footer(text="Hallucinate")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("✅")


    @commands.command(brief="Invites the bot to your server")
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Oooh, a new server!',
            description = "Want to add me to your server? Here\'s my link! \n[🤖 Bot invite](https://discord.com/api/oauth2/authorize?client_id=764513869526728705&permissions=8&scope=bot) \n [🙋‍♂️ Join our server!](https://discord.gg/VYEMZrkMRT) \n[🛠 GitHub](https://github.com/TransKat/HallucinateBot/)",
            colour = discord.Colour.green()

        )
        embed.set_footer(text="Hallucinate")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command(brief="SYLVEON")
    async def sylve(self, ctx):
        pic = random.randint(1,27)
        if pic == 6:
            await ctx.send(f"Sylveon #{pic}, Cosmo!")
        elif pic == 8:
            await ctx.send(f"Sylveon #{pic}, Sylvia!")
        elif pic == 10:
            await ctx.send(f"Cosmo and Kat! (#10)")
        elif pic == 12:
            await ctx.send(f"Sylveon #{pic}, Jacklyn!")
        else:
            await ctx.send(f"Sylveon #{pic}")
        await ctx.channel.send(file=discord.File(f'./sylveon/{pic}.png'))

    @commands.command(brief="SELECT YOUR SYLVEON")
    async def selectsylve(self, ctx, Sylveon:int):
        pic = Sylveon
        if pic == 6:
            await ctx.send(f"Sylveon #{pic}, Cosmo!")
        elif pic == 8:
            await ctx.send(f"Sylveon #{pic}, Sylvia!")
        elif pic == 10:
            await ctx.send(f"Cosmo and Kat! (#10)")
        elif pic == 12:
            await ctx.send(f"Sylveon #{pic}, Jacklyn!")
        else:
            await ctx.send(f"Sylveon #{pic}")
        await ctx.channel.send(file=discord.File(f'./sylveon/{pic}.png'))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! That took {(round(self.bot.latency*1000, 1))}ms')

def setup(bot):
    bot.add_cog(user(bot))
