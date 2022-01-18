from operator import truediv
from pydoc import cli
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix='%')
client.remove_command("help")

@client.event
async def on_ready():
    print("online")
    await client.change_presence(activity=discord.Game(name="%help"))

@client.command()
async def v(ctx):
    await ctx.send('Wersja 0.0.1')

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Lista komend", color=0xe20303)
    embed.add_field(name="%help", value="Spis komend", inline=False)
    embed.add_field(name="%yt", value="Informacje o Kanałach YT", inline=False)
    embed.add_field(name="%ttv", value="Informacje o Kanałach Twitch", inline=False)
    embed.add_field(name="%promo", value="Informacje o Dostępie do kanału Media", inline=True)
    embed.set_footer(text="Designed by Naznaczony")
    await ctx.send(embed=embed)

@client.command()
async def promo(ctx):
    embed=discord.Embed(title="Ranga MEDIA", description="Podanie o rangę media należy użyć ticked na kanale media podania inna forma zgłoszeń będzie odrzucana.", color=0x09e118)
    embed.set_footer(text="Naznaczony | BOT")
    await ctx.send(embed=embed)

@client.command()
async def yt(ctx):
    embed=discord.Embed(title="Kanały YouTube", color=0xe20303)
    embed.add_field(name="Naznaczony", value="https://www.youtube.com/c/NaznaczonyY", inline=False)
    embed.add_field(name="Jaseł", value="https://www.youtube.com/channel/UCEjmNl8G8pFJIRygiA5KLhg", inline=False)
    embed.set_footer(text="Designed by Naznaczony")
    await ctx.send(embed=embed)

@client.command()
async def ttv(ctx):
    embed=discord.Embed(title="Kanały Twitch", color=0xbb00ff)
    embed.add_field(name="n4znaczony", value="https://www.twitch.tv/n4znaczony", inline=False)
    embed.add_field(name="Jaseł", value="https://www.twitch.tv/jasels_ox", inline=False)
    embed.set_footer(text="Designed by Naznaczony")
    await ctx.send(embed=embed)

@client.command()
@has_permissions(ban_members=True)
async def embed(ctx, tutul, cos, cos2):
    embed=discord.Embed(title=tutul, color=0xe20303)
    embed.add_field(name=cos, value= cos2, inline=False)
    embed.set_footer(text="Ogłoszenie")
    await ctx.send(embed=embed)






@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member,reason="Bez Powodu"):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Zabnowano {member.mention} za {reason}")

@client.command()
@has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member,reason="Bez Powodu"):
    await member.kick(reason=reason)
    await ctx.channel.send(f"Wykopano {member.mention} za {reason}")









@client.event
async def on_member_join(member):
    kanal = discord.utils.get(member.guild.channels, id=932662647948718100)
    await kanal.send(f"{member.mention} Siema :)")

client.run('OTMyNTY0Njg1NDk5Mjc3MzYz.YeU0iw.3XxZj9BmS6g_L1UVuNP_EVrA5YE')
