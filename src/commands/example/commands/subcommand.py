import discord
from discord import app_commands
import os
import config

@app_commands.command(name="test", description="A test sub command")
async def command(interaction: discord.Interaction):
    await interaction.response.send_message("Test passed!")
    
async def setup(bot):
    global Bot 
    Bot = bot
    bot.tree.get_command("functions").add_command(command)    