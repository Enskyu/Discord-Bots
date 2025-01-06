import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="-", intents=intents)

# List to store messages
stored_messages = []

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check for duplicate messages
    is_duplicate = any(msg['content'] == message.content for msg in stored_messages)

    # Add the message to the list
    stored_messages.append({
        'author': str(message.author),
        'content': message.content,
        'channel': str(message.channel) if message.guild else "DM"
    })

    # Uncomment if you want to see who sent the message
    # print(f"Stored message from {message.author}: {message.content}")

    if is_duplicate:
        print("True")

    # Process commands if there are any
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def show(ctx):
    if not stored_messages:
        await ctx.send("No messages stored yet.")
    else:
        messages = [f"{msg['author']}: {msg['content']}" for msg in stored_messages]
        await ctx.send("\n".join(messages))

@bot.command()
async def clear(ctx):
    stored_messages.clear()
    await ctx.send("Stored messages have been cleared.")