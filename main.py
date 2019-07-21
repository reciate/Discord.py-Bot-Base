import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=['!'], description='A Simple Bot Base') #Here you can change the command prefix and the help message description
bot.owner_id = 0 #You must get your Discord ID by enabling Developer Mode and right clicking on your name and hitting Copy ID

for cog in ['cogs.example', 'cogs.base']: #This allows you to load cogs. The part before the dot is the folder name.
	bot.load_extension(cog)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('a game!')) #Here you can change the "playing" text for the bot.
    print('Logged in as ' + bot.user.name) #This is a response to the console once the bot is ready.
    print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + str(bot.user.id) + '&scope=bot&permissions=8')
    
#I would not recommend adding commands here since you cannot debug them in runtime without a restart.
	
@bot.command() #The next three commands allow you to load/unload cogs on the fly. You must set up bot.owner_id for these to work.
@commands.is_owner()
async def load(ctx, cog:str):
	try:
		bot.load_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.send('Cog ' + "'" + cog + "'" + ' has been loaded.')
		
@bot.command()
@commands.is_owner()
async def unload(ctx, cog:str):
	try:
		bot.unload_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.send('Cog ' + "'" + cog + "'" + ' has been unloaded.')
		
@bot.command()
@commands.is_owner()
async def reload(ctx, cog:str):
	try:
		bot.unload_extension(cog)
		bot.load_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.send('Cog ' + "'" + cog + "'" + ' has been reloaded.')

bot.run('TOKENHERE') #Get your bot token from https://discordapp.com/developers/applications/