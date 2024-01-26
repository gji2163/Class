import discord
from discord.ext import commands

TOKEN = 'ODQ2NzA2MjA1MDgyNTE3NTA1.YKzamg.lXLtjvSLeSvHLwVOnjDEFqaaPos'
bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.command(name='show', description="Greet the user!")
async def show(ctx):
    exec("x=io.BytesIO(base64.decodebytes(b'"+list(event.data.values())[0]+"'))")
    await ctx.send(f"Hello {ctx.author.name}!") # f-string
    await channel.send(file=discord.File(x))    

bot.run(TOKEN)
