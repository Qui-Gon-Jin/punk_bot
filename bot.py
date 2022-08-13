import discord
from datetime import datetime
from discord.ext import commands
import roll
import modules

client = discord.Client()
startup_time = datetime.now()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	print(str(startup_time))

@client.event
async def on_message(message):
	author = str(message.author).split('#')[0]
	if message.author == client.user:
		return
	#Help function call
	if message.content.startswith('!help'):
		await message.channel.send(modules.help())
	#Roll function call
	if message.content.startswith('!r'):
		roll_result = roll.roll(str(message.content), str(message.author))
		await message.channel.send(roll_result.rolling())
	#Count initiative call
	if message.content.startswith('!i'):
		initiative_result = roll.roll(str(message.content), str(message.author))
		await message.channel.send(initiative_result.initiative())

#Choose token for logining in discord API
token = open('token.txt', 'r')
client.run(token.read())
token.close()
