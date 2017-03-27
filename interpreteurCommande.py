import discord

class InterpreteurCommande:
	
	def __init__(self, cmdCarac):
		self.cmdCarac = cmdCarac
		
	async def interpreter(client, message):
		if message.content.startswith(cmdCarac):
			if message.content.startswith(cmdCarac + 'h') and message.author.id != client.user.id :
				await client.send_message(message.channel, '!help : affiche la listes de commmandes disponibles\n!bonjour : affiche un message de salutation\n!blague : une SUPER blague')
	
			elif message.content.startswith(cmdCarac + 'bonjour'):
				await client.send_message(message.channel, 'Bonjour bonjour ' + message.author.name + ' !')
		
			elif message.content.startswith(cmdCarac + 'blague'):
				await client.send_message(message.channel, 'Comment appelle ton un lapin sourd ?')
				await asyncio.sleep(10)
				await client.send_message(message.channel, 'Un LAAAAAPIIIIIN!!!')
				await asyncio.sleep(3)
				await client.send_message(message.channel, 'Voilà voilà')
