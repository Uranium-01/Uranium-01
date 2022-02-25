import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "u!", description = "Bot multifonction en cours de développement")

@bot.event
async def on_ready():
 	print ("Test réussi")

@bot.command()
async def serverinfo(ctx, *info):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfMember = server.member_count
	serverName = server.name
	message = f"{serverName} \n{serverDescription} \nNombre de membres : {numberOfMember} \nNombre de salons textuels : {numberOfTextChannels} \nNombre de salons vocaux : {numberOfVoiceChannels}"
 	if info == "" or info == " ":
		await ctx.send(message)
	elif info == "memberCount":
		message = f"Il y a {numberOfMember} membres sur ce serveur"
		await ctx.send(message)
	elif info == "numberOfChannels":
		message = f"Ce serveur contient {numberOfTextChannels} salons textuels et {numberOfVoiceChannels} salolns vocaux (Les salons provés ne sont pas comptés dans ces nombres)"
		await ctx.send(message)
	elif info == "name":
		message = f"Serveur {serverName}"
		await ctx.send(message)
	elif info == "numberofchannels" or info == "membercount" :
		await ctx.send("Etrange... Je ne connais pas cela \nEssayer d entrer *memberCount*, *numberOfChannels* ou *name* à la suite de votre commande \nVous pouvez aussi ne rien mettre si vous voulez voir toutes les info")
	else:
		ctx.send("Vous avez dû faire une erreur en tapant la commande \nTapez *u!serverinfo help* pour plus d informations")

@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def chinese(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))

bot.run("OTM5MDg3MzcxOTA1OTI1MTUw.YfzvRA.CKvmvLBKucm07UWCf8rVZFuXn6k")
