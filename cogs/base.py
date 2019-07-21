import discord
from discord.ext import commands

class Base(commands.Cog): #Make "Base" the file name.
	def __init__(self, bot):
		self.bot = bot
		
	
def setup(bot):
	bot.add_cog(Base(bot)) #Make "Base" the file name.
    
#You can directly copy and paste this base for however many cogs you would like. Ensure you change the names noted above.