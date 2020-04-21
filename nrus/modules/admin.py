import discord
from discord.ext import commands

from bot import NRus


class Admin(commands.Cog):
    def __init__(self, bot: NRus):
        self.bot = bot

    def cog_check(self, ctx):
        return self.bot.is_owner(ctx.author)

    @commands.command(hidden=True)
    async def reload(self, ctx: commands.Context, name: str) -> None:
        ext_name = f'modules.{name}'
        await ctx.send(f'Reloading {ext_name}')
        self.bot.reload_extension(ext_name)

    @commands.command(hidden=True)
    async def load(self, ctx: commands.Context, name: str) -> None:
        ext_name = f'modules.{name}'
        await ctx.send(f'Loading {ext_name}')
        self.bot.load_extension(ext_name)

    @commands.command(hidden=True)
    async def unload(self, ctx: commands.Context, name: str) -> None:
        ext_name = f'modules.{name}'
        await ctx.send(f'Unloading {ext_name}')
        self.bot.unload_extension(ext_name)

    @commands.command(hidden=True)
    async def loaded(self, ctx: commands.Context) -> None:
        e: discord.Embed = discord.Embed()
        e.add_field(name='Cogs Loaded:', value='\n'.join(self.bot.cogs))
        await ctx.send(embed=e)

    @commands.command(hidden=True, name='exec')
    async def exec_(self, ctx: commands.Context, *, text) -> None:
        text = text.strip('```python').strip('`').split('\n')
        out = ['async def f():']
        for line in text:
            out.append('\t'+line)
        vars_ = {'bot': self.bot, 'ctx': ctx}
        vars_ .update(globals())
        try:
            exec("\n".join(out), vars_)
            f = vars_['f']
            result = await f()
        except Exception as e:
            await ctx.send(f'{e.__class__}: {e}')
            return
        if result is not None:
            await ctx.send(result)


def setup(bot: NRus):
    bot.add_cog(Admin(bot))