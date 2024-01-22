import discord 
from discord.ext import commands
token='MTE5NzIxMzUxODMyODUwODUxNg.G2OTet.1zdC_rRv3nFJ8sHfAK6FF3ZWk9g9D_hzSFSUDU'
print(token)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready(): 
	guild_count = 0
	for guild in bot.guilds: 
		print(f"- {guild.id} (name: {guild.name})") 
		guild_count = guild_count + 1 
	print("MomentoMori is in " + str(guild_count) + " guilds.") 
    
@bot.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 
    
	#print(f'Message {user_message} by {username} on {channel}') 
	print(message)
	if message.author == bot.user: 
		return
	else:
		await message.reply(f'Hello {username}') 
		return
		

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
	
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(token)
