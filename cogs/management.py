from os import name
import discord
from discord import message
from discord import embeds
from discord import mentions
from discord.ext import commands

from discord_components import Button, ButtonStyle, SelectOption, Select, component
import discord_components


import os
import psutil
import random
import asyncio
import datetime
import time

from utils.json import loadjson, savejson


from discord.ext.commands.core import Command, command

class management(commands.Cog, name = "서버 관리 명령어", description = "서버 관리 명령어 Cog입니다."):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= '킥', aliases=['추방','kick'])
    @commands.has_permissions(administrator=True)
    async def mod_kick(self, ctx, member: discord.Member, *, reason: str = None):
        embed = discord.Embed(
            title = f"추방",
            description = f"유저를 킥했습니다.\n\n대상: {member}\n관리자: {ctx.author}\n사유: {reason}",
            colour = discord.Colour.dark_orange(),
            timestamp = ctx.message.created_at
        )
        await ctx.send(embed=embed)
        await member.send(embed = embed)
        await ctx.guild.kick(member, reason = reason)
    
    @commands.command(name= '밴', aliases=['차단','ban'])
    @commands.has_permissions(administrator=True)
    async def mod_ban(self, ctx, member: discord.Member, *, reason: str = None):
        embed = discord.Embed(
            title = "밴",
            description = f"유저를 밴했습니다.\n\n대상: {member}\n관리자: {ctx.author}\n사유: {reason}",
            colour = discord.Colour.red(),
            timestamp = ctx.message.created_at
            
        )
        await ctx.send(embed = embed)
        await member.send(embed = embed)
        await ctx.guild.ban(member, reason = reason)

    @commands.command(name= '뮤트', aliases = ["mute"])
    @commands.has_permissions(administrator=True)
    async def mod_mute(self, ctx,  user: discord.User, *,reason: str = None):
        embed = discord.Embed(title= "뮤트",description=f"{user} 유저에게 {reason}의 사유로 뮤트를 하시겠습니까?")
        tg = await ctx.send(embed=embed)
        await tg.add_reaction("✅")
        await tg.add_reaction("❌")
        def check(reaction, user):
            return (user == ctx.author and str(reaction) in ["✅","❌"] and tg.id == reaction.message.id)
        reaction, member = await self.bot.wait_for("reaction_add", check=check)
            

        if str(reaction) == '✅':
            role = discord.utils.get(ctx.guild.roles, name = "Muted")
            await ctx.guild.get_member(user.id).add_roles(role)
            embed= discord.Embed(title="뮤트",description=f"뮤트를 완료했습니다")
            await ctx.send(embed=embed)
        if str(reaction) == '❌':
            embed2= discord.Embed(title="뮤트",description=f"뮤트를 취소했습니다")
            await ctx.send(embed=embed2) 
    @commands.command(name= '언뮤트', aliases = ["unmute"])
    @commands.has_permissions(administrator=True)
    async def mod_unmute(self, ctx,  user: discord.User, *,reason: str = None):
        embed = discord.Embed(title= "뮤트",description=f"{user} 유저에게 언뮤트를 하시겠습니까?")
        tg = await ctx.send(embed=embed)
        await tg.add_reaction("✅")
        def check(reaction, user):
            return (user == ctx.author and str(reaction) in ["✅"] and tg.id == reaction.message.id)
        reaction, member = await self.bot.wait_for("reaction_add", check=check)
            

        if str(reaction) == '✅':
            role = discord.utils.get(ctx.guild.roles, name = "Muted")
            await ctx.guild.get_member(user.id).remove_roles(role)
            embed= discord.Embed(title="뮤트",description=f"언뮤트를 완료했습니다")
            await ctx.send(embed=embed)
    @commands.command(name="서버공지")
    @commands.has_permissions(administrator=True)
    async def notice_server(self, ctx, channel: discord.TextChannel, *, value):
        em = discord.Embed(
            title=f"{ctx.guild}공지사항",
            description=value,
            colour=discord.Colour.random()
        )
        em.set_footer(text="하람봇서포트서버랑 상관없는 이서버의 공지입니다.")
        await channel.send(embed=em)

    @commands.command(name = "청소", aliases = ["ㅊ"])
    @commands.has_permissions(administrator = True)
    async def clean(self, ctx, limit: int = None):
        if not type(limit) == int:
            return await ctx.reply("삭제할 수의 숫자 형식이어야 합니다.")
        await ctx.channel.purge(limit = limit + 1)
        await ctx.send(f"{limit}개의 메시지를 삭제하였습니다.", delete_after = 5)

    
    

def setup(bot):
    bot.add_cog(management(bot))
