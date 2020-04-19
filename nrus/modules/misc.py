from discord.ext import commands
from nrus.src.bot import NRus

class Misc(commands.Cog):
    def __init__(self, bot: NRus):
        self.bot = bot

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def set_prefix(self, ctx: commands.Context, prefix: str):
        self.bot.

def setup(bot: NRus) -> None:
    bot.add_cog(Misc)
