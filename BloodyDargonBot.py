import discord
import datetime
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    print("__________________")
    game = discord.Game("BloodyDargon Client")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!BloodyDargonBug"):
        await message.channel.send("Is this a bug on the server? Or is it a bug in the BloodDargon client?")
    if message.content.startswith("This is a bug in the server"):
        await message.channel.send("Please send a photo or message to guer457@gmail.com ^^")
    if message.content.startswith("This is a bug in the BloodyDargon client"):
        await message.channel.send("Please send a photo or message to guer457@gmail.com ^^")

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/Mute"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="Mute")
        await author .add_roles(role)

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="Mute")
        await author .remove_roles(role)

     if message.content.startswith("!안녕"):
         date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
         embed = discord.Embed(color=0xf0000)
         embed.add_field(name="이름", value=message.author.name, inline=True)
         embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
         embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
         embed.add_field(name="아이디", value=message.author.id, inline=True)
         await client.send_message(message.channel, embed=embed)


access-token - os.environ["BOT_TOKEN"]
client.run(access_token)


