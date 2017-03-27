import discord
import asyncio

import sys
from termcolor import colored

from interpreteurCommande import InterpreteurCommande

client = discord.Client()
interpreteurCommande = InterpreteurCommande('!')

@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
	print('id = ' + client.user.id)
	print('-----------------------------')
	
@client.event
async def on_message(message):
	print('[' + message.channel.name + ']\t' + colored(message.timestamp.strftime('%c'), 'green') + ': ' + color(message.author.name, message.author.color) + ' >\t' + message.content)
	
	#interpreteurCommande.interpreter(client, message)

def color(string, discordColor):
	resColor = 'grey'
	if discordColor== discordColor.gold():
		resColor = 'yellow'
	
	return colored(string, resColor)

client.run('Mjg4NjQ2Mzg5MzA5NzY3Njgw.C6CETw.b8jg3Bxp_21u_ggchKI9iNENzec')
