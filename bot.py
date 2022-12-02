import discord
import commands

async def send_message(message, user_message):
    try:
        response = commands.handle_command(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    print(discord.__version__)
    TOKEN = 'TOKEN'
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} in ({channel}).')

        await send_message(message, user_message)
    
    client.run(TOKEN)
