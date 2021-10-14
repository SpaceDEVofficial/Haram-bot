import io
import asyncio
import discord
from discord.ext import commands
class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = "핑"
    )
    async def ping(self, ctx):
        await ctx.send(embed = discord.Embed(title = "**Pong!**", description = f":ping_pong: {round(self.bot.latency) * 1000}ms", color= 0x0000ff))

def setup(bot):
    bot.add_cog(general(bot))
