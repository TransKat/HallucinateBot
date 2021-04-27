import discord
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

    @commands.command(brief="Sends a message for you")
    async def say(self, ctx, arg):
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(brief="Generates a random number from 0 to a number of your choice.")
    async def gennumber(self, ctx, arg):
        output = random.randint(0,(int(arg)))
        await ctx.send(output)

    @commands.command(brief="Info about the current server.")
    async def serverinfo(self, ctx):
        icon = ctx.guild.icon_url
        await ctx.send(f"Name: {ctx.guild.name}\nID: {ctx.guild.id}\nOwner: {ctx.guild.owner_id}\nBoosts: {ctx.guild.premium_subscription_count}\nCreated: {ctx.guild.created_at}\nIcon: {icon}")

    @commands.command(brief="Invites the bot to your server")
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Oooh, a new server!',
            description = "Want to add me to your server? Here\'s my link! \n[🤖 Bot invite](🛠 https://discord.com/api/oauth2/authorize?client_id=764513869526728705&permissions=8&scope=bot) \n[🙋‍♂️ Join our server!](https://discord.gg/VYEMZrkMRT) \n[GitHub](https://github.com/TransKat/HallucinateBot/)",
            colour = discord.Colour.green()

        )
        embed.set_footer(text="Hallucinate")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(user(bot))
