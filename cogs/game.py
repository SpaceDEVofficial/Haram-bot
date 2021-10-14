from os import name
import discord
from discord import message
from discord import embeds
from discord.ext import commands

import os
import psutil
import random
import asyncio
import datetime
import time


from discord.ext.commands.core import Command, command


class game(commands.Cog, name = "게임 명령어", description = "게임 명령어 Cog입니다."):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name = "가위바위보"
    )
    async def rsp_cmd(self, ctx):
        m = await ctx.send(f"<@{ctx.author.id}> 안 내면 진다 가위 바위 보")
        await m.add_reaction('✌')
        await m.add_reaction('✊')
        await m.add_reaction('🖐')
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == ctx.author and str(reaction.emoji) in ['✌', '✊', '🖐'])
        except asyncio.TimeoutError:
            await ctx.send(f'<@{ctx.author.id}>\n어? 안냈내? 그럼 내가 이겨따!!^^')
        else:
            if str(reaction.emoji) == "✌":
                a = ['가위','보','바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"쳇. 비겼네......;;",color=discord.Colour.yellow(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"ㄲㅂ. 내가 이겨야 하는데... 그래 내가 한판 봐줬다. 니가 이겼어",color=discord.Colour.red(), timestamp=ctx.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"거봐 내가 이긴다고 했지? 에휴. 허접이네",color=discord.Colour.blue(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
            elif str(reaction.emoji) == "✊":
                a = ['가위','보','바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"ㄲㅂ. 내가 이겨야 하는데... 그래 내가 한판 봐줬다. 니가 이겼어",color=discord.Colour.red(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"거봐 내가 이긴다고 했지? 에휴. 허접이네",color=discord.Colour.blue(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"쳇. 비겼네......;;",color=discord.Colour.yellow(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
            elif str(reaction.emoji) == "🖐":
                a = ['가위','보','바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"거봐 내가 이긴다고 했지? 에휴. 허접이네",color=discord.Colour.blue(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"쳇. 비겼네......;;",color=discord.Colour.yellow(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"ㄲㅂ. 내가 이겨야 하는데... 그래 내가 한판 봐줬다. 니가 이겼어",color=discord.Colour.red(), timestamp=ctx.message.created_at)
                    embed.add_field(name=f"{ctx.author}", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{self.bot.user.name}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    
    @commands.command(
        name = "주사위"
    )
    async def dice(self, ctx):
        await ctx.send(f"{random.randint(2, 12)}가 나왔습니다!")





def setup(bot):
    bot.add_cog(game(bot))