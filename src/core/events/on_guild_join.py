import discord
from discord.ext import commands
from core.functions.initilize_guild import initilize_guild
import config 
     
class onguildjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if config.connect_db:
          await initilize_guild(guild, self.bot)
                 
         
async def setup(bot):
    global Bot
    Bot = bot

    await bot.add_cog(onguildjoin(bot))         
