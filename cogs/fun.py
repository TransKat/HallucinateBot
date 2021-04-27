import discord
import random
import time
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="yeets a user")
    async def yeet(self, ctx, member: discord.Member, *, arg):
        await ctx.reply(f"{member.mention} was yeeted by <@{ctx.author.id}>! \nReason: {arg}")

    @commands.command(brief="Warms someone up")
    async def warm(self, ctx, user:discord.Member):
        await ctx.reply(f"{ctx.author.mention} warmed up {user.mention}.")

    @commands.command(brief="Cools someone down")
    async def cool(self, ctx, user:discord.Member):
        await ctx.reply(f"{ctx.author.mention} cooled down {user.mention}.")

    @commands.command(brief="Sends a message in embed form.")
    async def embedsay(self, ctx, *, arg):
        await ctx.message.delete()
        embed = discord.Embed(
            title = ' ',
            description = arg,
            colour = discord.Colour.green()

        )
        await ctx.reply(embed=embed)

    @commands.command(brief="Sends a message for you")
    async def say(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)
        print(f"{ctx.author} used h.say to send {arg} in {ctx.channel.id}")

    @commands.command(brief="Generates a random number from 0 to a number of your choice.")
    async def gennumber(self, ctx, arg):
        output = random.randint(0,(int(arg)))
        await ctx.reply(output)


    @commands.command(brief="Generates a random number from 0 to 5000")
    async def random(self, ctx):
        num = random.randrange(0,5000)
        await ctx.reply(f"{ctx.author.mention}, the result was {num}")
        await ctx.message.add_reaction("✅")

    @commands.command(brief="Take a chance! Will you survive a 75 meter fall?")
    async def leap(self, ctx):
        height = random.randint(70,80)
        value = random.randint(0,12)
        await ctx.reply(f"You fell off of a crane {height} meters up!")
        time.sleep(1)
        if value == 0:
            await ctx.send("Every bone in your body is in pieces. You died.")
        elif value == 1:
            await ctx.send("You lived, but you'll never walk again.")
        elif value == 2:
            await ctx.send("You died. Next time, don't land on your skull.")
        elif value == 3:
            await ctx.send("You managed to land into a pool, and you lived. You'll live the rest of your life with back pain.")
        elif value == 4:
            await ctx.send("The force from hitting the ground ruptured your lungs. You died.")
        elif value == 5:
            await ctx.send("You had a big umbrella, which slowed your fall enough to where you're not a puddle on impact. You still broke an arm, but you lived.")
        elif value == 6:
            await ctx.send("Your body snapped in half on impact. You bled out shortly and died.")
        elif value == 7:
            await ctx.send("You hit a tree shortly before hitting the ground, breaking your fall for a second. You lived, but broke your left leg.")
        elif value == 8:
            await ctx.send("You clip into the ground upon hitting it, and somehow survive.")
        elif value == 9:
            await ctx.send("As you fell, a slime smacked into you, resetting your fall speed and launching you into a nearby balcony, where you only suffered a few minor injuries. The slime, unfortunately, did not survive.")
        else:
            await ctx.send("There was a failsafe and you lived.")

def setup(client):
    client.add_cog(fun(client))
