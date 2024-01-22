import pathlib
import textwrap
import discord 
from discord.ext import commands

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyAOfH7s9Y0YPDSZb93BX9RbHMwkU8x1E1s'
token='MTE5NzIxMzUxODMyODUwODUxNg.G2OTet.1zdC_rRv3nFJ8sHfAK6FF3ZWk9g9D_hzSFSUDU'


genai.configure(api_key=GOOGLE_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

'''for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)'''

model = genai.GenerativeModel('gemini-pro')
'''response = model.generate_content("Hi, I am Anurag")
for chunk in response:
  print(chunk.text)
  print("_"*80)
to_markdown(response.text)
print(response.text)'''
y='y'

@bot.event 
async def on_ready(): 
	guild_count = 0
	for guild in bot.guilds: 
		print(f"- {guild.id} (name: {guild.name})") 
		guild_count = guild_count + 1 
	print("FEDBOT is in " + str(guild_count) + " guilds.") 
     
chat= model.start_chat(history=[])
@bot.event 
async def on_message(message,chat=chat): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 
    
	#print(f'Message {user_message} by {username} on {channel}') 
	print(message.content)
	if message.author == bot.user: 
		return
	else:
		response=chat.send_message(message.content)
		if len(response.text)>2000:
			response=chat.send_message("make it short under 2000characters")
		await message.reply(response.text) 
		print(chat.history)
		return

'''while(y in ['Y','y']):
  msg=input('user: ')
  response=chat.send_message(msg)
  print("bot: "+response.text)
  y=input("do you want to continue? y/n : ")

print(chat.history)'''

bot.run(token)