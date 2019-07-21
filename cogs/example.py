import discord
from discord.ext import commands

#This is an example cog to show how commands can be added

class Example(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command() #Use this to define that a command is starting
	async def ping(self, ctx): #Definition of the function. Always pass through self and ctx (context) when in a cog. Self is not needed in main.
        #Command description that is shown in the help command
		'''
		Pong!
		'''
		await ctx.send('Pong!') #Sends a chat message. Remember to await async functions.
		
	@commands.command()
	async def inviteurl(self, ctx):
		'''
		Generates an invite link for the bot
		'''
		await ctx.send('https://discordapp.com/oauth2/authorize?&client_id=' + str(self.bot.user.id) + '&scope=bot&permissions=8')
		
def setup(bot):
	bot.add_cog(Example(bot))