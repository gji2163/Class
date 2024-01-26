import discord

TOKEN = "ODQ2NzA2MjA1MDgyNTE3NTA1.YKzamg.lXLtjvSLeSvHLwVOnjDEFqaaPos"
#GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_ready():
    for guild in client.guilds:
        #if guild.name == GUILD:
         #   break

        print(f'{client.user}:\n{guild.name}(id: {guild.id})\n')

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    print(f'Greetings {member}, welcome to {member.guild.name}') 

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Greetings {member.name}, welcome to {member.guild.name}!')

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)
