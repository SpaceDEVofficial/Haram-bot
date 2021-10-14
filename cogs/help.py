import io
import asyncio
from PycordPaginator import Paginator
import discord
from discord import colour
from discord.ext import commands

from cogs.util import util


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    @commands.command(name="도움말", aliases=['도움'])
    async def pagination(self, ctx):
        global embeds
        main = discord.Embed(
            title = "메인",
            description="""
안녕하세요! 하람봇을 사용해주셔서 감사합니다!

도움말 메뉴는 아래와 같습니다

1️⃣|1. 메인페이지
2️⃣|2. 서버관리페이지 🔰 
3️⃣|3. 코로나페이지 🧬
4️⃣|4. 유틸리티페이지 🧰
5️⃣|5. 게임페이지 🕹️
            
[서포트서버](https://discord.gg/Jk6VRvsnqa)
            
            
        """,
        colour=discord.Colour.random()
        )
        main.set_footer(text=f"1 / 5페이지",icon_url=ctx.author.avatar_url)


        manage = discord.Embed(
            title="서버 관리 🔰",
            description="""
서버관리 명령어를 사용해보세요!     
모든 관리명령어는 관리자 권한을
가진 사람들만 사용할수 있습니다.
""",
            colour=discord.Colour.random()
        )
        manage.add_field(name="하람아 추방 @유저",
                         value="```\n맨션된 유저를 추방을 해요\n```",
                         inline=False)
        manage.add_field(name="하람아 밴 @유저",
                         value="```\n맨션된 유저를 차단을 해요\n```",
                         inline=False)
        manage.add_field(name="하람아 뮤트 @유저",
                         value="```\n맨션된 유저를 뮤트를 해요\n```",
                         inline=False)
        manage.add_field(name="하람아 언뮤트 @유저",
                         value="```\n맨션된 유저를 언뮤트을 해요\n```",
                         inline=False)
        manage.add_field(name="하람아 서버공지 [작성]",
                         value="```\n자신의 서버에 공지를 올려요!\n```",
                         inline=False)
        manage.add_field(name="하람아 청소 [갯수]",
                         value="```\n메시지를 청소를 해요!\n```",
                         inline=False)
        manage.set_footer(text=f"2 / 5페이지",icon_url=ctx.author.avatar_url)

        covid = discord.Embed(
            title="코로나 🧬",
            description="""
코로나 명령어를 사용해보세요!
코로나 현황을 알려드립니다
""",
            colour=discord.Colour.random()
        )
        covid.add_field(name="하람아 코로나현황",
                        value="```\n현재 코로나현황을 알려드립니다.\n```",
                        inline=False)
        covid.set_footer(text=f"3 / 5페이지",icon_url=ctx.author.avatar_url)

        utili = discord.Embed(
            title="유틸리티 🧰",
            description="""
유틸리티 명령어를 사용해보세요!

  
            """,
            colour=discord.Colour.random()
        )
        utili.add_field(name="하람아 유저정보 @유저",
                        value="```\n맨션한 유저정보를 보여줍니다\n```",
                        inline=False)
        utili.add_field(name="하람아 내정보 @유저",
                        value="```\n당신의 정보를 보여줍니다\n```",
                        inline=False)
        utili.add_field(name="하람아 서버정보",
                        value="```\n지금 있는 서버정보를 보여줍니다\n```",
                        inline=False)
        utili.add_field(name="하람아 프사",
                        value="```\n당신의 프사를 보여줍니다\n```",
                        inline=False)
        utili.add_field(name="하람아 프사 @유저",
                        value="```\n맨션한 유저의 프사를 보여줍니다\n```",
                        inline=False)
        utili.set_footer(text=f"4 / 5페이지",icon_url=ctx.author.avatar_url)


        games=discord.Embed(
            title="게임 🕹️",
            description="""
게임명령어를 사용해서
미니게임을 해보세요!
            """,
            colour=discord.Colour.random()
        )
        games.add_field(name="하람아 가위바위보",
                        value="```\n가위바위보 게임\n```",
                        inline=False)
        games.add_field(name="하람아 주사위",
                        value="```\n주사위를 돌려 누가 많이 나오는지 \n 내기를 해보세요!\n```",
                        inline=False)
        games.set_footer(text=f"5 / 5페이지",icon_url=ctx.author.avatar_url)
        desc = {
            "메인 페이지": "메뉴가 있는 메인페이지",
            "서버 관리 🔰": "서버 관리 명령어가 있는 페이지.",
            "코로나 🧬": "코로나 명령어가 있는 페이지",
            "유틸리티 🧰":"유틸리티 명령어가 있는 페이지",
            "게임 🕹️":"게임 명령어가 있는 페이지"
        }

        embeds = [main,manage,covid,utili,games]
        e = Paginator(
            client=self.bot.components_manager,
            embeds=embeds,
            channel=ctx.channel,
            only=ctx.author,
            ctx=ctx,
            use_select=True,
            desc=desc)
        await e.start()

def setup(bot):
    bot.add_cog(help(bot))
