import discord
from discord.ext import commands
import random

def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def findimpostor(self, ctx):
        """Impostors can sabotage the reactor. 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win."""


        # determining
        embed1 = discord.Embed(title = "Who's the impostor?" , description = "Find out who the impostor is, before the reactor breaks down!" , color=0xff0000)
        
        # fields
        embed1.add_field(name = 'Red' , value= '⛔' , inline=False)
        embed1.add_field(name = 'Blue' , value= '🔵' , inline=False)
        embed1.add_field(name = 'Lime' , value= '✅' , inline=False)
        embed1.add_field(name = 'White' , value= '⚪' , inline=False)
        
        # sending the message
        msg = await ctx.send(embed=embed1)
        
        # emojis
        emojis = {
            'red': '⛔',
            'blue': '🔵',
            'lime': '✅',
            'white': '⚪'
        }
        
        # who is the impostor?
        impostor = random.choice(list(emojis.items()))
        impostor = impostor[0]
        
        # for testing...
        print(emojis[impostor])
        
        # adding choices
        for emoji in emojis.values():
            await msg.add_reaction(emoji)
        
        # a simple check, whether reacted emoji is in given choises.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try: 
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        
        except TimeoutError:
            # reactor meltdown - defeat
            description = "Reactor Meltdown.{0} was the impostor...".format(impostor)
            embed = get_embed("Defeat", description, discord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory
            if str(self.reacted) == emojis[impostor]:
                description = "**{0}** was the impostor...".format(impostor)
                embed = get_embed("Victory", description, discord.Color.blue())
                await ctx.send(embed=embed)

            # defeat
            else:
                for key, value in emojis.items(): 
                    if value == str(self.reacted):
                        description = "**{0}** was not the impostor...".format(key)
                        embed = get_embed("Defeat", description, discord.Color.red())
                        await ctx.send(embed=embed)
                        break

    @commands.command(brief="Can you guess the number?s")
    async def jackpot(self, ctx, guess=None):
        num = random.randint(0,10)
        if int(guess) == num:
            await ctx.send(f"You win! The number was {num}.")
        elif guess == None:
            await ctx.send("You need to guess something zero to ten!")
        elif int(guess) >= 11:
            await ctx.send("You need to guess something zero to ten!")
        elif int(guess) <= -1:
            await ctx.send("You need to guess something zero to ten!") 
        else:
            await ctx.send(f"Aw. You lost. The number was {num}, while you guessed {guess}.")

def setup(bot):
    bot.add_cog(games(bot))